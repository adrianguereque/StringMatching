# O(n)
def manacher(string):
  texto = string.lower()
  texto = texto.replace(' ', '')
  texto = '$'.join(f'^{texto}$')
  n = len(texto)
  P = [0] * n

  centro = limite = 0

  for i in range(1, n - 1):
    if i < limite:
      simetrica = 2 * centro - i
      P[i] = min(limite - i, P[simetrica])

    gap = P[i] + 1
    while texto[i - gap] == texto[i + gap]:
      P[i] += 1
      gap += 1
    if i + P[i] > limite:
      limite = i + P[i]
      centro = i

  max_len, centro_index = max((n, i) for i, n in enumerate(P))
  start = (centro_index - max_len) // 2

  return string[start: start + max_len]