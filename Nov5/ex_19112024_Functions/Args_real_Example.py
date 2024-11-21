def pizza_toppings(*toppings):
    for i in toppings:
        print(i)
A=pizza_toppings("cheese","butter")
B= pizza_toppings("chicken","cheese","butter")
C=pizza_toppings("corn","chicken","butter","cheese")
#Ouput=cheese butter
 #      chicken cheese butter
 #corn,chicken,butter,cheese
def pizza_toppings(*toppings):
    print(toppings)
    for i in toppings:
        print(i)
A=pizza_toppings("cheese","butter")
B= pizza_toppings("chicken","cheese","butter")
C=pizza_toppings("corn","chicken","butter","cheese")

#output=('cheese', 'butter')
#cheese
#butter
#('chicken', 'cheese', 'butter')
#chicken
#cheese
#butter
#('corn', 'chicken', 'butter', 'cheese')
#corn
#chicken
#butter
#cheese
