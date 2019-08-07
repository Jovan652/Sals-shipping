def ground_shipping(weight):
  if weight <= 2:
    return (weight * 1.5) + 20
  elif weight > 2 and weight < 6:
    return (weight * 3.0) + 20
  elif weight > 6 and weight < 10:
    return (weight * 4.0) + 20
  else: 
    return (weight * 4.75) + 20
  
premium_shipping = 125

def drone_shipping(weight):
  if weight <= 2:
    return (weight * 4.5) 
  elif weight > 2 and weight < 6:
    return (weight * 9.0)
  elif weight > 6 and weight < 10:
    return (weight * 12.0)
  else: 
    return (weight * 14.25)
  
print(ground_shipping(8.4))
print(drone_shipping(1.5))

def cheapest(weight):
  ground = ground_shipping(weight)
  premium = premium_shipping
  drone = drone_shipping(weight)
  if ground < premium and ground < drone:
    method = 'standard ground'
    cost = ground
  elif premium < ground and premium < drone:
    method = 'premium ground'
    cost = premium
  else:
    method = drone
    cost = drone
    
  print('The cheapest option available is $%.2f with %s shipping '  
  % (cost, method))
cheapest(1)


