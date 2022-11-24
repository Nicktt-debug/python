h = int(input())
m = int(input())
s = int(input())


s = s +1
s_mod = s // 60
s_rsd = s % 60
s_fin = s_rsd

m = m + s_mod
m_mod = m // 60
m_rsd = m % 60
m_fin = m_rsd

h_fin = h + m_mod
h_fin = h_fin%24

print(h_fin,m_fin,s_fin)