from Crypto.Util.number import long_to_bytes, inverse
from sympy import symbols, solve

# 已知数据
n = 120786335084751534030676597784517268197341222014914446913320445991646463021521467181164536499859787748785082948444634749797338257305524925366466238635023797470657555232565198644631189968666979202194498505639522031424533509199241421928738962178651688983118892898107569406220912960261234864718043752108160555117
c1 = 30747630924129553784494459690772685701382128170425288341458647725247855419005560917367498647667613099482457671768276365147256313308363517423408589587338973655970573105987238072393172798903074848756366374998964687865697156016751729396174713279646099857914687259266796294381668062986281746206817703184644052749
c2 = 30747630924129553784494459690772685701382128170425288341458647725247855419005560917367460594203590517910343569812601792047236727073342445054991004339650534617458578513011694528225031720351281390748744203653766468027135003691251869418823672489695666389690330808331586984408731287279167710147815445748285739902
e = 3

# 枚举可能的 Δm
for delta in range(-(2**32), 2**32):
    # 假设 c1 - c2 = Δm * (m1^2 + m1 * m2 + m2^2)
    delta_c = c1 - c2
    if delta_c % delta != 0:
        continue

    # 恢复 m1 和 m2 的结构
    potential_sum = delta_c // delta
    m = symbols("m", integer=True)

    # 解方程 m^2 + (m << 32) + (m << 32)^2 = potential_sum
    solution = solve(m**2 + m * (m << 32) + (m << 32) ** 2 - potential_sum, m)
    for sol in solution:
        if sol > 0:  # 筛选出正数的解
            flag = long_to_bytes(sol)
            print(f"Recovered FLAG: {flag}")
            break
