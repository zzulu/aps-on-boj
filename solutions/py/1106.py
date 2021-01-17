# def ad(customer, N, hotel, min_cost):
#     if customer <= 0:
#         return 0

#     if min_cost[customer]:
#         return min_cost[customer]

#     minimum = 100*1000
#     for n in range(N):
#         cost = ad(customer-hotel[n][1], N, hotel, min_cost) + hotel[n][0]
#         if cost < minimum:
#             minimum = cost
#     min_cost[customer] = minimum
#     return minimum


C, N = map(int, input().split())

hotel = [[0, 0] for _ in range(20)]
dp = [0]*(100*1000+1)

for n in range(N):
    cost, customer = map(int, input().split())
    hotel[n] = [cost, customer]

for n in range(N):
    for cost in range(hotel[n][0], 100*1000+1):
        dp[cost] = max(dp[cost], dp[cost - hotel[n][0]] + hotel[n][1]);

for cost, customer in enumerate(dp):
    if customer >= C:
        print(cost)
        break
