route_stack = [[0,0]]
route_history = [[0,0]]
source=[ 
    [0,0,1,0,1],
    [1,0,0,0,1],
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,0,0,1,0]]
def up(location):
    
    if location[1] == 0:
        return False
    else:
        new_location = [location[0],location[1]-1]
        if new_location in route_history:
            return False
        elif source[new_location[0]][new_location[1]] == 1:
            return False
        else:
            route_stack.append(new_location)
            route_history.append(new_location)
            return True
 
def down(location):
    if location[1] == 4:
        return False
    else:
        new_location = [location[0],location[1]+1]
        if new_location in route_history:
            return False
        elif source[new_location[0]][new_location[1]] == 1:
            return False
        else:
            route_stack.append(new_location)
            route_history.append(new_location)
            return True
 
def left(location):
    if location[0] == 0:
        return False
    else:
        new_location = [location[0]-1,location[1]]
        if new_location in route_history:
            return False
        elif source[new_location[0]][new_location[1]] == 1:
            return False
        else:
            route_stack.append(new_location)
            route_history.append(new_location)
            return True
 
def right(location):
    if location[0] == 4:
        return False
    else:
        new_location = [location[0]+1,location[1]]
        if new_location in route_history:
            return False
        elif source[new_location[0]][new_location[1]] == 1:
            return False
        else:
            route_stack.append(new_location)
            route_history.append(new_location)
            return True
lo = [0,0]
while route_stack[-1] != [4,4]:
    if up(lo):
        lo = route_stack[-1]
        continue
    if down(lo):
        lo = route_stack[-1]
        continue
    if left(lo):
        lo = route_stack[-1]
        continue
    if right(lo):
        lo = route_stack[-1]
        continue
    route_stack.pop()
    lo = route_stack[-1]
print route_stack
