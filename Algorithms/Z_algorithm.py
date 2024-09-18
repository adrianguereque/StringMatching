# O(n + m) donde n es texto y m patron
def Z_algorithm(patron, texto):
  L = R = 0
  C = patron + '$' + texto
  n = len(patron)
  m = len(texto)
  x = n + m + 1
  Z = [-1] * x
  for i in range(1, x):
    if i <= R:
      k = i - L
      if Z[k] < R - i + 1:
        Z[i] = Z[k]
      else:
        L = i
        while R < x and C[R - L] == C[R]:
          R += 1
        Z[i] = R - L
        R -= 1
    else:
      L = R = i
      while R < x and C[R - L] == C[R]:
        R += 1
      Z[i] = R - L
      R -= 1
  return Z

def get_matches(patron, texto):
    Z = Z_algorithm(patron, texto)
    n = len(patron)
    indexes = []
    for i in range(n + 1, len(Z)):
        if Z[i] == n:
            indexes.append(i - (n + 1))

    return indexes