print("1. addition");
print("2. subtraction");
print("3. multiplication");
print("4. division");
print("5. exit");
choice=int(input("enter your choice: "));
if (choice>=1 and choice<=4):
   print("enter two number: ");
num1 = int(input());
num2 = int(input());
if choice == 1:
    res = num1 + num2;
    print("result = ", res);
if choice == 2:
    res = num1 - num2;
    print("result =",res);
if choice ==3:
    res = num1 * num2;
    print("result =", res);
else:
    res = num1 /num2;
    print("result =", res);
if choice == 5:
    exit();
else:
    print("wrong input..!!");
