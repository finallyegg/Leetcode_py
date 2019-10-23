# def sortedSquares(self, A):
#     """
#     :type A: List[int]
#     :rtype: List[int]
#     """
#     i = 0;
#     while A[i] <= 0:
#         A[i] = pow(A[i], 2);
#         i += 1;
#
#     j = i - 1;
#     retval = [];
#     while (j >= 0 | i < len(A)):
#         if (A[j] < pow(A[i]), 2):
#             retval.append(A[j]);
#             j -= 1;
#         else:
#             retval.append(pow(A[i], 2);
#             i += 1;
#     while j >= 0:
#         retval.append(A[j]);
#         j -= 1;
#     while i < len(A):
#         retval.append(pow(A[i], 2));
#         i += 1;
#     a = [];
#     sorted([])
#     return A
#
#     def imageSmoother(self, A):
#         """
#         :type M: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         i = len(A);
#         j = len(A[0]);
#         if i==1 and j==1:
#             print(123)
#         for x in range(0, i):
#             for y in range(0, j):
#                 if i == j == 1:
#                     A[x][y] = A[x][y]
#                 elif x == 0 and y == 0:
#                     A[x][y] = (A[0][0] + A[0][1] + A[1][0] + A[1][1]) // 4
#                 else if x == 0 and y == j - 1
#                     A[x][y] = (A[x][y - 1] + A[x][y] + A[x + 1][y - 1] + A[x + 1][y]) // 4
#                 else if x == i-1 and y == 0:
#                     A[x][y] = (A[x - 1][y] + A[x - 1][y + 1] + A[x][y] + A[x][y + 1]) // 4
#                 else if x == i - 1 and y == j - 1:
#                     A[x][y] = (A[x - 1][y - 1] + A[x - 1][y] + A[x][y - 1] + A[x][y]) // 4
#                 else if x == 0:
#                     A[x][y] = (A[x][y - 1] + A[x][y] + A[x][y + 1] +
#                                A[x + 1][y - 1] + A[x + 1][y] + A[x + 1][y + 1]) // 6
#                 else if x == i - 1:
#                     A[x][y] = (A[x - 1][y - 1] + A[x - 1][y] + A[x - 1][y + 1] +
#                                A[x][y - 1] + A[x][y] + A[x][y + 1]) // 6
#                 else if y == 0:
#                     A[x][y] = (A[x - 1][y] + A[x - 1][y + 1] +
#                                A[x][y] + A[x][y + 1] +
#                                A[x + 1][y] + A[x + 1][y + 1]) // 6
#                 else if y == j - 1:
#                     A[x][y] = (A[x - 1][y - 1] + A[x - 1][y] +
#                                A[x][y - 1] + A[x][y] +
#                                A[x + 1][y - 1] + A[x + 1][y]) // 6
#                 else:
#                     A[x][y] = (A[x - 1][y - 1] + A[x - 1][y] + A[x - 1][y + 1] +
#                                A[x][y - 1] + A[x][y] + A[x][y + 1] +
#                                A[x + 1][y - 1] + A[x + 1][y] + A[x + 1][y + 1]) // 9
#         return A

def p1loss(x1,x2):
    return pow(x1,2)+pow(x2,2);

def p1gradient(x1,x2):
    return [2*x1,2*x2];

def p4gradient(x1,x2,h):
    orginLoss = p1loss(x1,x2);
    dx1 = (p1loss(x1+h,x2)-orginLoss)/h;
    dx2 = (p1loss(x1,x2+h)-orginLoss)/h;
    return [dx1,dx2];

def computeLoss(x1,x2,itor,learningrate):
    for i in range (1,itor+1):
        x1 = x1 - learningrate*p1gradient(x1,x2)[0];
        x2 = x2 - learningrate*p1gradient(x1,x2)[1];
    return [x1,x2]
print(p1gradient(20,20));
print("\n");
print(computeLoss(3,0.25,1,0.2));
# print(p1loss(2,3));