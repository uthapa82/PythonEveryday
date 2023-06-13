def main():
    test_cases = int(input("Enter the number of Test cases: "))
    for i in range(test_cases):
        try: 
            a, b = map(str, input("Enter a & b: ").split())
            print(int(a)//int(b))
        except Exception as e:
            print("Error code: ", e)
            
if __name__ == '__main__':
    main()
        