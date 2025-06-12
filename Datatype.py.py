a={
                'public_id': "user.public_id",
                'first_name':"user.first_name",
                'last_name':"user.last_name",
                'email':"user.email",
                'phone_number':[{"user":"phone_number"}],
                'password':("user","password"),
                'Token': {"tokens",'access'},
                'refresh': frozenset({"tokens","refresh"})
               
            }
#print( type(frozenset({"tokens","refresh"})))

#given data is dict then findout the value of phone_numner ,
#  if phone_number value is list then find out element datatype , 
# if first element data type is dict then value of user , 
# if user value is string then reverse that str print reversed string otherwise print nothing to do 


if type(a) == dict:
    print(a["phone_number"])
    if type(a["phone_number"]) ==  list:
        print(type(a["phone_number"]))
        if type(a["phone_number"][0]) == dict:
            print(a["phone_number"][0]["user"])
            if type(a["phone_number"][0]["user"]) == str:
                print("before reversing the string is ",a["phone_number"][0]["user"])
                print("After reversing the string is",a["phone_number"][0]["user"][-1::-1] )
            else:
                print("Nothing to do")