import os

def WIN_GAME():
	print "\n\n+~*YOU WIN THE GAME!!!*~+\n"
	ok = raw_input("\n\nCONTINUE...[Enter]")

def LOSE_GAME():
	print "\n\n +~*YOU LOSE*~+\n"
	ok = raw_input("\n\nCONTINUE...[Enter]")
	exit()

"""ACTIVE: Prints out the postition. Does not change"""
def print_player_position(x,y):
    if (x==0):
        if (y==0):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            | (You) |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting
	    $$$ = Door"""
        elif(y==1):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            % (You) |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==2):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            | (You) |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==3):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            | (You) |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
            
    elif (x==1):
        if(y==0):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       | (You) |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==1):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       | (You) |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==2):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       | (You) |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==3):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       | (You) #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
            
    elif (x==2):
        if(y==0):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |       | (You) |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==1):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |       | (You) |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==2):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |       | (You) | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==3):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |       # (You) #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""

    elif (x==3):
        if(y==0):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |       |       | (You) |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==1):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |       |       | (You) |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==2):
            pass
        elif(y==3):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |       #       # (You) |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
    
    elif (x==4):
        if(y==0):
            pass
            
        elif(y==1):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |	    #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |       |       |       | (You) |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==2):
            pass
        elif(y==3):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |       #       #       | (You) |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
    
    elif (x==5):
        if(y==0):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |       #       #       |       |       +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |	    |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed | (You) |       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==1):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |       #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |       +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       | (You) |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==2):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |       #       #       |       |	    +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table | (You) +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |       |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
        elif(y==3):
            print """

            |########################++++++###++++++########|
            |    Bathroom   #Closet #       |       |       +
            |       |       #       #       |       | (You) +       
            |       |       #       #       |       |       +
            |##########-----###----##-----------------------|
            |       |       |       |#######|#######|       +
            |       |	    |       | Chair | Table |	    +       
            |       |       |       |#######|#######|       +
            |-----------------------------------------------|
            %       |       |       |       |       |       |
            %       |	    |       |       |       |       |       
            %       |       |       |       |       |       |
            |-----------------------------------------------|
            |       |       |       |       |#######|#######|
            |       |	    |       |       |#  Bed |#######|       
            |       |       |       |       |#######|#######|
            |################$$$$$$$########################|

            (You) = Your Position
            ### = Impassable wall / furniture
            +++ = Windows
            %%% = Painting 
	    $$$ = Door"""
            
    else:
        print "I do not understand your request."

"""ACTIVE: Gives new x value to x_position"""
def new_moved_x(user_input, x, y):
    if user_input == 'd': 
		if (y==0):
			if (x == 3) or (x==5):
				return x
			else:
				new_x = x + 1
				return new_x
		elif (y==1):
			if(x==5):
				return x
			else:
				new_x = x + 1
				return new_x
		elif (y==2):
			if (x == 2) or (x==5):
				return x
			else:
				new_x = x + 1
				return new_x
		elif (y==3):
			if (x==1) or (x==2) or (x==5):
				return x
			else:
				new_x = x + 1
				return new_x		
    elif user_input == 'a':
		if (y==0):
			if (x == 0) or (x==5):
				return x
			else:
				new_x = x - 1
				return new_x
		elif (y==1):
			if (x == 0):
				return x
			else:
				new_x = x - 1
				return new_x
		elif (y==2):
			if (x == 0) or (x==5):
				return x
			else:
				new_x = x - 1
				return new_x
		elif (y==3):
			if (x == 0) or (x==3) or (x==2):
				return x
			else:
				new_x = x - 1
				return new_x
    else:
        return x

"""ACTIVE: Gives new y value to y_position"""
def new_moved_y(user_input, x, y):
    if user_input == 'w':
		if (y==1):
			if (x==3) or (x==4):
				return y
			else:
				new_y = y +1
				return new_y
		elif(y==2):
				if (x==0):
					return y
				else:
					new_y = y +1
					return new_y
		elif(y==3):
			return y
		else:
			new_y = y + 1
			return new_y
    elif user_input == 's':
		if (y==0):
			return y
		elif (y==1):
			if (x==4):
				return y
			else:
				new_y = y - 1
				return new_y
		elif(y==3):
				if (x==0) or (x==3) or (x==4):
					return y
				else:
					new_y = y -1
					return new_y
		else:
			new_y = y - 1
			return new_y
    else:
        return y

"""ACTIVE: Shows list of commands"""
def show_help():
	print """
	_Commands:_
	*Must be typed in all lowercase!*
	
	inventory - Checks inventory.
	look around - Look around the area.
	pick up <item_name> - Picks up item.
	use <item> - Use an item in your inventory.
	examine <item> - Examines item in inventory.
	drop <item> - Drops item onto area.
	break <item> - Breaks the item.

	"""
	ok = raw_input("CONTINUE... [Enter]")

"""ACTIVE: Shows Inventory"""
def show_inventory(m,bm,h,w,n,l,k,ha,no):
	print "_Inventory:_\n"
	if m:
		print "*Mirror"
	if bm:
		print "*Broken Mirror"
	if h:
		print "*Hammer"
	if w:
		print "*Wrench"
	if n:
		print "*Nail"
	if l:
		print "*Lamp"
	if k:
		print "*Key"
	if ha:
		print "*Hanger"
	if no:
		print "*Note"
	ok = raw_input("\nCONTINUE... [Enter]")
	
"""IN-PROGRESS (NEED DESCRIPTIONS): Response to Look Around"""	
def show_description(x,y,t):
	if (y==0):
		if (x==0):
			pass
		elif (x==1):
			pass
		elif (x==2):
			pass
		elif (x==3):
			if not(t):
				t = introduction(t)
			found_trap_door()
			return t
		elif (x==4):
			pass
		elif (x==5):
			if not(t):
				t = introduction(t)
			found_trap_door()
			return t
				
	elif (y==1):
		if (x==0):
			if not(t):
				pass
		elif (x==1):
			pass
		elif (x==2):
			pass
		elif (x==3):
			if not(t):
				t = introduction(t)
			found_trap_door()
			return t
		elif (x==4):
			if not(t):
				t = introduction(t)
			found_trap_door()
			return t
		elif (x==5):
			if not(t):
				t = introduction(t)
			found_trap_door()
			return t
	elif (y==2):
		if (x==0):
			pass
		elif (x==1):
			pass
		elif (x==2):
			pass
		elif (x==3):
			pass
		elif (x==4):
			pass
		elif (x==5):
			pass
	elif (y==3):
		if (x==0):
			pass
		elif (x==1):
			pass
		elif (x==2):
			pass
		elif (x==3):
			pass
		elif (x==4):
			pass
		elif (x==5):
			pass
	
"""ACTIVE: Pick_up command"""
def pick_up(x,y,have_item,loc, item_name):
	if not(have_item) and loc[0]==x and loc[-1]==y:
		print "\n\nYou picked up a %s!" % item_name
		ok = raw_input("\n\nCONTINUE...[Enter]")
		return not(have_item)
	elif have_item:
		print "\n\nYou tried to pick up something you can't find..."
		print "\n\nAnd failed miserably."
		ok = raw_input("\n\nCONTINUE...[Enter]")
	
"""IN-PROGRESS: examine command"""
def examine(item,m,bm,h,w,n,l,k,ha,no):
	if str(item)[8:]=='mirror':
		if m:
			print "\n\nIt's a small, hand-held mirror. Whoever made it did not glue "
			print "the glass properly-it's ready to fall out.\n"
			ok = raw_input("CONTINUE...[Enter]")
		else:
			print "\n\n You do not have this item.\n"
			ok = raw_input("CONTINUE...[Enter]")
	elif str(item)[8:]=='broken mirror':
		if bm:
			print "\n\nOh, you worst of the worst Cro-Magnons! Your ugly face broke it! "
			print "Now you have a bunch of dangerous mirror shards that are only dangerous "
			print "at one end, but safe enough to be held with three fingers at the other end!\n"
			ok = raw_input("CONTINUE...[Enter]")
		else:
			print "\n\n You do not have this item.\n"
			ok = raw_input("CONTINUE...[Enter]")
	elif str(item)[8:]=='hammer':
		if h:
			print "\n\nA regular hammer for pounding people's heads-er, "
			print "you mean, nails-in. \n"
			ok = raw_input("CONTINUE...[Enter]")
		else:
			print "\n\n You do not have this item.\n"
			ok = raw_input("CONTINUE...[Enter]")
	elif str(item)[8:]=='wrench':
		if w:
			print "\n\nThis is obviously a wrench despite the fact there is a "
			print "star-shaped-opening instead of a U-opening. You know. Obviously. \n"
			ok = raw_input("CONTINUE...[Enter]")
		else:
			print "\n\n You do not have this item.\n"
			ok = raw_input("CONTINUE...[Enter]")
	elif str(item)[8:]=='nail':
		if n:
			print "\n\nThe nail, though inanimate, is very heavy and menacing in your hand. "
			print "The head of it almost seems to be screaming,"
			print "\"I'll nail your eyes in if you star at me any longer!\" \n"
			ok = raw_input("CONTINUE...[Enter]")
		else:
			print "\n\n You do not have this item.\n"
			ok = raw_input("CONTINUE...[Enter]")
	elif str(item)[8:]=='lamp':
		if l:
			print "\n\nThis is a lamp. Maybe this could be useful... or "
			print "not... Perhaps you should do the logical thing and drop it.\n"
			ok = raw_input("CONTINUE...[Enter]")
		else:
			print "\n\n You do not have this item.\n"
			ok = raw_input("CONTINUE...[Enter]")
	elif str(item)[8:]=='hanger':
		if ha:
			print "\n\nWhat do you do if you don't hook a fish? Hanger! Get it? Hang... her...?\n"
			print "...The steel hanger with an abnormally long neck burns icy cold.\n"
			ok = raw_input("CONTINUE...[Enter]")
		else:
			print "\n\n You do not have this item.\n"
			ok = raw_input("CONTINUE...[Enter]")
	elif str(item)[8:]=='note':
		if no:
			print "\n\nNear the end"
			print "Use your killer tool with its partner in crime"
			print "The use your strangely shaped object to retrieve"
			print "Your only hope to survive.\n"
			ok = raw_input("CONTINUE...[Enter]")
		else:
			print "\n\n You do not have this item.\n"
			ok = raw_input("CONTINUE...[Enter]")
	elif str(item)[8:]=='key':
		if k:
			print "\n\nA tool for getting people out of rooms filled with water"
			print "that's rising as you speak. That's the power of "
			print "the Key +coughbladecough+!\n"
			ok = raw_input("CONTINUE...[Enter]")
		else:
			print "\n\n You do not have this item.\n"
			ok = raw_input("CONTINUE...[Enter]")
	else:
		print "\n\n You don't even have this item...\n"
		ok = raw_input("CONTINUE...[Enter]")
	
	
"""-------DESCRIPTIONS----------"""
def introduction(n):
	print """
	
		Before you is the frameless
		bed that you just got off of.

		...You yawn.
	
		...You still feel pretty groggy. 
		Like, really, REALLY groggy.  
		Groggy enough for a good idea 
		to float into your brain. 
		That is, perhaps you should just 
		go back to sleep. 

		...I mean, THE WATER FLOODING 
		THE ROOM IS NO CAUSE FOR ALARM, right?
	
		Your heart aches a little. With sarcasm
		like this, who needs sidekicks? 
		Sighing, you swish the water toward the bed,
		hitting the frame. Your big toe instantly 
		swells against your shoe...

		...but wait. Frame? You blink. The bed is
		FRAMELESS! That's what you said ten lines 
		ago. So what did you hit...?
	
		You kneel and poke your head underneath 
		the bed, and consequently under the water, 
		which causes your open eyes to begin 
		STINGING LIKE CRAZY. 
	
		But a quick glance was enough to discern 
		the source of the heavy or hard thing 
		your toe met. It was a metal chain... 
		hooked to some sort of door.
	
		...Could it be a way out...?
		"""
	
	ok = raw_input("CONTINUE...[Enter]")
	if not(n):
		return not(n)
	else: 
		return n
def found_trap_door():
	print "\n\nThis door really piques your interest... Should you check it out?[y] or [n]"
	ok = raw_input("\n\n>>> ")
	if (str(ok)=='y'):
		print """
		
		You decide to throw all your hopes of 
		leaving this room onto this mysterious 
		door beneath the bed. 
		
		(...Of course, you're not LITERALLY 
		THROWING ANYTHING onto this door. 
		Well, besides yourself.)
		
		Taking a deep breath, you plunge your 
		head into the water and feel the floor 
		for the chain. Once your hand seizes the 
		chain, you slowly pull yourself toward 
		the handle the chain is hooked to. 
		Then, with as much force as you can 
		muster while your eyes are shut and 
		you're still feeling groggy...
		
		UNDERWATER... you tug on the handle.
	
		For a moment, nothing happens. But you 
		don't waver. You want to get out of this 
		room, darn it!
	
		So you tug. """
	
		ok = raw_input("\n\nCONTINUE...[Enter]")
	
		print "\n\n\t\tAnd tug."
	
		ok2 = raw_input("\n\nCONTINUE...[Enter]")
	
		print "\n\n\t\tAnd tug."
	
		ok3 = raw_input("\n\nCONTINUE...[Enter]")
		
		os.system('cls')
		
		print """
		And come out of the water for an occasional 
		inhale of fresh oxygen. After the tenth tug, 
		you feel yourself drifting outward with the 
		door handle. In exhilaration, you pop your 
		head out of the water for a little more air 
		before diving right back in...
	
		...and meeting the razor-sharp teeth of an alligator. 
	
		Screaming, or at least you would be if you 
		were ABOVE the water, and flailing your arms, 
		you attempt to swim away from the alligator. 
		But it's too fast! Surprisingly! 
		Like a Titan from Shingeki no Kyoujin, 
		it hungrily reaches for you with its mouth... 
		and succeeds.
	
		In less than three seconds, it leaps forward 
		in the water and consumes you whole. As you 
		feel its teeth clamp down on your face, 
		you give yourself one last set of hurtful 
		remarks.
	
		YOU HOOLIGAN. 

		WHY WOULD THE WAY OUT OF THE ROOM BE 
		UNDERNEATH A FRAMELESS BED? YOU BETTER 
		NOT DO THAT IN YOUR NEXT LIFE. 
	
		(But of course, there's no way that in
		your next life that you would end up in
		a room again...)

		~~GAME OVER~~
		"""
	
		ok4 = raw_input("\n\nCONTINUE...[Enter]")
		exit()	
	elif (str(ok)=='n'):
		print "\n\nNAH!!!"
		ok = raw_input("\n\nCONTINUE...[Enter]")		
def painting_before_tear():
	print """
	You stare in awe. 
	What a beautiful painting that's 
	hang up on this wall. 
	You continue staring until you 
	realize yet again that the floor 
	is filling up water, you walk away 
	thinking,"It would be such a shame if 
	anything were to happen to it..."
	"""
	ok4 = raw_input("\n\nCONTINUE...[Enter]")
def painting_after_use_mirror():
	print """
	The painting now lies in front of you 
	torn to bits. You seem to notice the key 
	behind the frame on the painting but there 
	is a barrier in the way. There is also a 
	hole with five sharp points. You wonder 
	what this is for...
	"""
	ok4 = raw_input("\n\nCONTINUE...[Enter]")
def painting_after_use_hammer_and_nail():
	print"""
	Earlier, you finally understood that 5 pointed shaped was a 
	STAR and had used the hammer with the star-shaped-nail.
	
	Now, the key seems closer than ever! 
	But it's way too far to reach...
	
	How the heck am I supposed to reach that FAR!?
	"""
	ok4 = raw_input("\n\nCONTINUE...[Enter]")
def painting_after_use_hanger():
	print"""
	The once beautiful painting is ruined. 
	The key that was once hidden there is also gone.
	You are able to get the key!
	"""
	ok4 = raw_input("\n\nCONTINUE...[Enter]")
def door():
	print "\n\nIt is a door. Nothing of interest. Move along now.\n"
	ok = raw_input("...[Enter]\n")
	print "NO WAIT A MINUTE YOU FOUND THE WAY OUT omg omg GET THAT DOOR OPEN!"
	print "\n..."
	print "\n..."
	print "\n..."
	ok = raw_input("\n...[Enter]\n")
	print "EXCEPT THERE'S NO HANDLE, DOORKNOB, BUTTON, OR"
	print "MOTION-SENSOR DEVICE THAT WILL LET THE DOOR OPEN\n"
	print "Still, you try throwing your body, fist, foot, and head against it."
	print "Like the time that mean bully, who was two feet taller than you," 
	print "stood there as you bounced off like a ball, you bounce off the door" 
	print "and plummet into the water. For several minutes, you are tearing at" 
	print "the surface of the water, desperately gasping for air.\n"
	print "Then you realize the water only reaches your neck.\nSo you quickly get"
	print "back up and examine yourself. While your body, fist, and foot suffered"
	print "minimal damage, you're not sure your head got off so easily-you are" 
	print "feeling groggy.\n"
	print "Shaking your head-as if that would fix your grogginess-you contemplate"
	print "every decision you ever made that made you make such a colossal mistake"
	print "the simplest of Cro-Magnon would have avoided it."
	print "And then you try breaking the door again\n"
	ok = raw_input("...[Enter]\n")
	print "You stop when your finger gets is somehow mercilessly slashed by"
	print "the sharp edges of a keyhole you ALSO somehow missed in your initial" 
	print "examination of this door.\n"
	ok = raw_input("...[Enter]\n")
def closet():
	print "\n\nYou have found yourself in a small walk-in closet with a shelf." 
	print "On the shelf sits a tool, probably a wrench. Beneath"
	print "it are twenty articles of clothing hanging-faux fur jackets, snow" 
	print "jackets, biker jackets, faux leather jackets,"
	print "and chili red leather snow jackets that are"
	print "actually for REALLY RAINY DAYS in London.\n"
	print "Of course, you've never been to London. But that's not the important thing here."
	print "The important thing is that... you are in a small walk-in closet.\n"
	ok = raw_input("\n...[Enter]\n")
	print "A small walk-in closet."
	ok = raw_input("\n...[Enter]\n")
	print "A small closet."
	ok = raw_input("\n...[Enter]\n")
	print "A closet."
	ok = raw_input("\n...[Enter]\n")
	print "A..."
	ok = raw_input("\n...[Enter]\n")
	print "...MAGICAL WARDROBE TO NARNIA!!! YEAHHHHHHHHHHHH WE'RE GETTING OUT OF THIS ROOM\n"
	ok = raw_input("...[Enter]\n")
	print "With glee that cannot be adequately described in a no-budget Python game, you"
	print "dramatically push away the heavy jackets. But the jackets don't move. So you" 
	print "then decide to squeeze your way through them. As you go farther into the closet" 
	print "and away from the water-filled room, you feel your heart lift." 
	print "Your soul is becoming lighter. And then-"
	ok = raw_input("\n...[Enter]\n")
	print "And then your face abruptly hits a hanger with a really long neck that"
	print "does not have clothing on it."
	ok = raw_input("\n...[Enter]\n")
	print "Darn."
	print "There was no magical wardrobe escape route after all."
	ok = raw_input("\n...[Enter]\n")
def table(r):
	print "\n\nAn old and dusty chair alongside an old and dusty table"
	print "sits before you. You have an urge to make it less dusty"
	print "by intelligently putting your hand on the table instead"
	print "of spending time looking for a way out. But just as you"
	print "are about to do so, your eye notices a clock and a note.\n"
	ok = raw_input("\n...[Enter]\n")
	print "\nThe clock reads: %d \n" % (r)
	ok = raw_input("\n...[Enter]\n")
	print "You're not sure what that means, but you,re"
	print "CERTAIN you have PLENTY of TIME left."
	ok = raw_input("\n...[Enter]\n")
	print "As for the note, it reads: \n"
	print "\tNear the end"
	print "\tUse your killer tool with its partner in crime"
	print "\tThen use your strangely-shaped object to retrieve"
	print "\tYour only hope to survive.\n"
	print "Unfortunately, you did not even comprehend any of this."
	print "But no matter! Surely, you can escape without understanding a" 
	print "suspiciously-placed cryptic riddle note and a "
	print "suspiciously-placed cryptic clock. "
	ok = raw_input("\n...[Enter]\n")
def window_1():
	print """
	Boarded-up windows mock your sanity on your right. 
	
	Of course, you do the logical thing of ramming your head 
	into it after coming to the conclusion that the windows 
	on the right are boarded. I mean, the bulls and turtles 
	did it back at the ranch. 
	
	As your head hurts (AGAIN) you're starting to wonder if 
	you have greater problems beyond being stuck in this room
	filling up with water at an extremely high rate.
	
	But you don't have time to think about that. Right now, 
	you've got to get those windows open! 
	
	Even though they're clearly boarded up PRETTY tight.

	"""
	ok = raw_input("\n...[Enter]\n")
def window_2():
	print """
	MORE boarded-up windows mock your sanity on your other other other left. 
	
	(In other words, your right.)
	
	This time, you refrain from butting your head in anything. You have 
	suffered enough damage by your above-average intelligence 
	already. Instead, you run your fingers against the rough wood 
	nailing the windows shut. 

	Then, out of nowhere, you shriek, "Ow!" 
	
	...For no reason in particular. One doesn't HAVE to shriek "ow" if one 
	gets a splinter in your finger AND stub one's toe against the other 
	toe. Which, by the way, did NOT happen to you. 
	
	Instead, you had shouted "ow" because an itsy-bitsy teeny weeny part
	of your finger's skin was torn open by a star-shaped nail head. 
	
	Really.
	"""
	ok = raw_input("\n...[Enter]\n")
def bathroom():
	print """
	You seemed to have entered the bathroom...yup there's 
	the bathtub and a toilet...
	
	AHHHH!! WHAT THE HECK IS THAT?!... Oh it's just your own 
	reflection in the handheld mirror that's just standing up 
	against the sink faucet for perfectly normal reasons. Just
	a typical old handheld...
	
	You then turn your attention to the bathtub to check to 
	see if anything's in there...
	
	Eww... it looks like no one has used this thing in ages 
	and it's filled with a bunch of junk! Like a hammer! 
	Obviously nothing that will help you...
	"""
	ok = raw_input("\n...[Enter]\n")
def fish():
	print """
	You decide to pause in your search to look around, but at the moment
	you decided to look around, you happened to have your head in the 
	water. (Unfortunately, you cannot remember what wonderful idea 
	impelled you to put your head in the water.) 
	
	So you only see your feet. 
	
	Suddenly, a severe sadness seizes your heart. 
	
	"WHERE ARE THE FISHES?" you cry out.
	"""
	ok4 = raw_input("\n\nCONTINUE...[Enter]")
"""--------ITEMS--------"""
mirror = 'Mirror'
have_mirror = False
mirror_loc = [0,3]

brokenMirror = 'Broken Mirror'
have_brokenMirror = False
broken_mirror_location = [0,0]

hammer = 'Hammer'
have_hammer = False
hammer_loc = [0,3]

wrench = 'Wrench'
have_wrench = False
wrench_loc = [2,3]

nail = 'Nail'
have_nail = False
nail_1_loc = [3,3]

lamp = 'Lamp'
have_lamp = False
lamp_loc = [5,2]

key = 'Key'
have_key = False
key_loc = [0,1]
key_dropped = False

hanger = 'Hanger'
have_hanger = False
hanger_loc = [2,3] 

note = 'Note'
have_note = False
note_loc = [4,1]

"""--------START--------"""

saw_intro = False
ripped_painting = False
broke_barrier_in_painting = False
used_hanger_in_paint_to_get_key = False
broke_mirror = False

MOVES_AVAILABLE = 100
MOVES_REMAINING = MOVES_AVAILABLE

val_x = 5
val_y = 0
yo = 0
os.system('cls')
print """
...

...

...

...A sharp pain sears through the right side of your head. 
As you sit up from a moldy frameless bed, you tentatively 
brush your fingers across your temple, and open your eyes.

"""
ok = raw_input("...[Enter]\n")
os.system('cls')
print """

Before you is a dimly-lit bedroom. Directly in front of 
you is a worn out chair and table. Farther back are two
boarded-up windows. To your immediate left, there is 
some kind of frame. There appears to be two doors in 
the corner. 

"""
ok = raw_input("...[Enter]\n")
os.system('cls')
print "You immediately start questioning yourself.\n"
print "'Where the heck am I? How did I get here? "
print "Who put me here? Why me? WHYYYYYYYYYYYYYYYYYYYYYYYYYYY?!'\n"
print "But unsurprisingly, no one gives you answers your demands for answers. You're not schizophrenic.\n"
print "...yet.\n"
ok = raw_input("...[Enter]\n")
os.system('cls')
print """
So instead, you try rubbing both temples. 
But nothing comes to mind. Not even your name. 
All you know is that you're in a closed room.

"""
ok = raw_input("...[Enter]\n")
os.system('cls')
print """
Or at least, it seems closed. You adopt 
the gesture of an old sage playing with his beard
and quickly conclude it'd be most ideal to get 
off the frameless bed and investigate the room. 

"""
ok = raw_input("...[Enter]\n")
os.system('cls')
print """
Still feeling dizzy, you are about to swing your 
feet onto the floor when the sound of water 
suddenly enters your ears.

"""
ok = raw_input("...[Enter]\n")
os.system('cls')
print """
Your whole body freezes. Your right eye twitches. 
Your mouth quivers. The water... is very close by. 

"""
ok = raw_input("...[Enter]\n")
os.system('cls')
print """
You gulp, already coming to conclusions as 
you peek over the bed...

"""
ok = raw_input("...[Enter]\n")
os.system('cls')
print """
...and see that the whole floor is flooded 
with water that seems to rise with every other blink.

"""
ok = raw_input("...[Enter]\n")
os.system('cls')
print """
Your head suddenly clears.

You have to get out. 

Now.

"""
ok = raw_input("...[Enter]\n")
while yo == 0:
	os.system('cls')
	print print_player_position(val_x,val_y)
	print "[w] Up\n[s] Down\n[a] Left\n[d] Right\n\nType 'help' for more commands."
	OPTION = raw_input("\n\n>>> ")
	val_x = new_moved_x(OPTION,val_x, val_y)
	val_y = new_moved_y(OPTION,val_x, val_y)
	if (OPTION=='help'):
		show_help()
	elif (OPTION=='inventory'):
		show_inventory(have_mirror, have_brokenMirror, have_hammer, have_wrench, have_nail,have_lamp,have_key,have_hanger,have_note)
	elif (OPTION=='look around'):
		if (val_x==3 and val_y==0) or (val_x==3 and val_y==1) or (val_x==4 and val_y==1) or (val_x==5 and val_y==1) or (val_x==5 and val_y==0):
			saw_intro = show_description(val_x,val_y, saw_intro)
		elif (val_x==0 and val_y==1):
			if not(ripped_painting):
				painting_before_tear()
			elif ripped_painting and broke_barrier_in_painting and used_hanger_in_paint_to_get_key:
				painting_after_use_hanger()
			elif ripped_painting and broke_barrier_in_painting:
				painting_after_use_hammer_and_nail()
			elif ripped_painting:
				painting_after_use_mirror()
		elif (val_x==2 and val_y==0):
			door()
		elif (val_x==2 and val_y==3):
			closet()
		elif (val_x==2 and val_y==2):
			table(MOVES_REMAINING)
		elif (val_x==5 and val_y==2) or (val_x==5 and val_y==3):
			window_1()
		elif (val_x==3 and val_y==3) or (val_x==4 and val_y==3):
			window_2()
		elif (val_x==0 and val_y==3) or (val_x==1 and val_y==3):
			bathroom()
		else:
			fish()
	elif (str(OPTION).startswith('pick up ')):
		if str(OPTION)[8:]=='mirror':
			if not(have_mirror) and not(broke_mirror):
				have_mirror = pick_up(val_x, val_y,have_mirror,mirror_loc, mirror)
			else:
				print "\n\nYou tried to pick up something you already have..."
				print "\n\nAnd failed miserably."
				ok = raw_input("\n\nCONTINUE...[Enter]")
		elif str(OPTION)[8:]=='hammer':
			if not(have_hammer):
				have_hammer = pick_up(val_x, val_y,have_hammer,hammer_loc, hammer)
			else:
				print "\n\nYou tried to pick up something you already have..."
				print "\n\nAnd failed miserably."
				ok = raw_input("CONTINUE...[Enter]")
		elif str(OPTION)[8:]=='wrench':
			if not(have_wrench):
				have_wrench = pick_up(val_x, val_y,have_wrench,wrench_loc, wrench)
			else:
				print "\n\nYou tried to pick up something you already have..."
				print "\n\nAnd failed miserably."
				ok = raw_input("CONTINUE...[Enter]")
		elif str(OPTION)[8:]=='nail':
			if have_wrench:
				if not(have_nail):
					have_nail = pick_up(val_x, val_y,have_nail,nail_1_loc, nail)
				else:
					print "\n\nYou tried to pick up something you already have..."
					print "\n\nAnd failed miserably."
					ok = raw_input("\n\nCONTINUE...[Enter]")
			else:
				print "\n\nYou failed to get the nail. You probably need a certain item...."
				ok = raw_input("\n\nCONTINUE...[Enter]")
		elif str(OPTION)[8:]=='lamp':
			if not(have_lamp):
				have_lamp = pick_up(val_x, val_y,have_lamp,lamp_loc, lamp)
			else:
				print "\n\nYou tried to pick up something you already have..."
				print "\n\nAnd failed miserably."
				ok = raw_input("CONTINUE...[Enter]")
		elif str(OPTION)[8:]=='hanger':
			if not(have_hanger):
				have_hanger = pick_up(val_x, val_y,have_hanger,hanger_loc, hanger)
			else:
				print "\n\nYou tried to pick up something you already have..."
				print "\n\nAnd failed miserably."
				ok = raw_input("CONTINUE...[Enter]")
		elif str(OPTION)[8:]=='note':
			if not(have_note):
				have_note = pick_up(val_x, val_y,have_note,note_loc, note)
			else:
				print "\n\nYou tried to pick up something you already have..."
				print "\n\nAnd failed miserably."
				ok = raw_input("CONTINUE...[Enter]")
		elif str(OPTION)[8:]=='key':
			if not(key_dropped):
				print "\n\nYou tried to pick up something that is not there..."
				print "\n\nAnd failed miserably."
				ok = raw_input("CONTINUE...[Enter]")
			elif key_dropped:
				if not(have_key):
					have_key = pick_up(val_x, val_y,have_key,key_loc, key)
				else:
					print "\n\nYou tried to pick up something you already have..."
					print "\n\nAnd failed miserably."
		else:
			print "\n\nYou can't pick that up!"
			ok = raw_input("CONTINUE...[Enter]")
	elif (str(OPTION).startswith('use ')):  
		if str(OPTION)[4:]=='mirror':
			if have_mirror:
				print "You stare at yourself. That was pretty useless..."
			else:
				print "You do not have this object."
		elif str(OPTION)[4:]=='broken mirror':
			if have_brokenMirror:
				if ripped_painting:
					print "\n\nYou already vandalized this painting..."
					ok = raw_input("\n\nCONTINUE...[Enter]")
				else:
					if ((val_x==0) and (val_y==1)):
						ripped_painting = True
						painting_after_use_mirror()
					else:
						print "\n\nYou can't use that here! You dolt!"
						ok = raw_input("\n\nCONTINUE...[Enter]")
			else:
				print "\n\nYou do not have this object."
				ok = raw_input("\n\nCONTINUE...[Enter]")
		elif str(OPTION)[4:]=='hammer':
			if have_hammer:
				if ((val_x==0) and (val_y==1)):
					if ripped_painting:
						if broke_barrier_in_painting:
							print "\n\nYou already nailed this painting..."
							ok = raw_input("\n\nCONTINUE...[Enter]")
						else:
							if have_nail:
								broke_barrier_in_painting = True
								painting_after_use_hammer_and_nail()
							else:
								print "\n\nYou can't use this item unless you have a nail..."
								ok = raw_input("\n\nCONTINUE...[Enter]")
					else:
						print "\n\nYou can't use this item... yet."
						ok = raw_input("\n\nCONTINUE...[Enter]")
				else:
					print "\n\nYou can't use that here! You dolt!"
					ok = raw_input("\n\nCONTINUE...[Enter]")
			else:
				print "\n\nYou do not have this object."
				ok = raw_input("\n\nCONTINUE...[Enter]")
		elif str(OPTION)[4:]=='wrench':
			if have_wrench:
				print "\n\nYou swing the object around and almost broke your wrist."
				print "You should stop now..."
				ok = raw_input("\n\nCONTINUE...[Enter]")
			else:
				print "\n\nYou do not have this object."
				ok = raw_input("\n\nCONTINUE...[Enter]")
		elif str(OPTION)[4:]=='nail':
			if have_nail:
				if ((val_x==0) and (val_y==1)):
					if ripped_painting:
						if broke_barrier_in_painting:
							print "\n\nYou already nailed this painting..."
							ok = raw_input("\n\nCONTINUE...[Enter]")
						else:
							if have_hammer:
								broke_barrier_in_painting = True
								painting_after_use_hammer_and_nail()
							else:
								print "\n\nYou can't use this item unless you have a nail..."
								ok = raw_input("\n\nCONTINUE...[Enter]")
					else:
						print "\n\nYou can't use this item... yet."
						ok = raw_input("\n\nCONTINUE...[Enter]")
				else:
					print "\n\nYou can't use that here! You dolt!"
					ok = raw_input("\n\nCONTINUE...[Enter]")
			else:
				print "\n\nYou do not have this object."
				ok = raw_input("\n\nCONTINUE...[Enter]")
		elif str(OPTION)[4:]=='lamp':
			if have_lamp:
				print "/n/nThe lamp shines brightly before you."
				print "Your eyes hurt now."
				ok = raw_input("\n\nCONTINUE...[Enter]")
			else:
				print "/n/nYou do not have this item..."
				ok = raw_input("\n\nCONTINUE...[Enter]")
		elif str(OPTION)[4:]=='hanger':
			if have_hanger:
				if ((val_x==0) and (val_y==1)):
					if ripped_painting and broke_barrier_in_painting:
						used_hanger_in_paint_to_get_key = True
						painting_after_use_hanger()
						key_dropped = True
					else:
						print "\n\nYou can't use this item yet!"
						ok = raw_input("\n\nCONTINUE...[Enter]")
				else:
					print "\n\nYou are not using this in the right area!"
					ok = raw_input("\n\nCONTINUE...[Enter]")
			else:
				print "/n/nYou do not have this item..."
				ok = raw_input("\n\nCONTINUE...[Enter]")
		elif str(OPTION)[4:]=='note':
			if have_note:
				print "/n/nThe note shines brightly before you."
				print "Your eyes hurt now."
				ok = raw_input("\n\nCONTINUE...[Enter]")
			else:
				print "/n/nYou do not have this item..."
				ok = raw_input("\n\nCONTINUE...[Enter]")
		elif str(OPTION)[4:]=='key':
			if have_key:
				if ((val_x==2) and (val_y==0)):
					WIN_GAME()
					exit()
				else:
					print "\n\nYou can't do that here..."
					ok = raw_input("\n\nCONTINUE...[Enter]")	
			else:
				print "\n\nYou do not have the key!!!"
				ok = raw_input("\n\nCONTINUE...[Enter]")
		else:
			print "That is not a real item to use!"
			ok = raw_input("\n\nCONTINUE...[Enter]")
	elif (str(OPTION).startswith('examine ')):   
		examine(str(OPTION),have_mirror, have_brokenMirror, have_hammer, have_wrench, have_nail,have_lamp,have_key,have_hanger,have_note)
	elif (str(OPTION).startswith('drop ')):
		if str(OPTION)[5:]=='lamp':
			print "\n\nYou have done it! You've realized the only way"
			print "to get out of this place is to throw this lamp on"
			print "the floor because water and electricity totally mix!"
			print "\nYou throw it at the ground and you suddenly feel a"
			print "sense of electricity all around your body... Oh right."
			print "\nElectricity and water don't go together."
			LOSE_GAME()
		else:
			print "\n\nFor some reason, your inner hoarder in you"
			print "does not want to let the item go. You decided"
			print "to stay with the item..."
			ok = raw_input("\n\nCONTINUE...[Enter]")
	elif (str(OPTION).startswith('break ')):
		if str(OPTION)[6:]=='mirror':
			if have_mirror:
				print "\n\nYou break the mirror and receive a"
				print "broken mirror and 7 years bad luck."
				have_mirror = False
				have_brokenMirror = True
				broke_mirror = True
				ok = raw_input("\n\nCONTINUE...[Enter]")
			else:
				print "\n\nYou do not have a mirror..."
				ok = raw_input("\n\nCONTINUE...[Enter]")
	elif (str(OPTION)=='allitemsplz'):
		have_mirror = True
		have_brokenMirror = True
		have_hammer = True
		have_wrench = True
		have_nail = True
		have_lamp = True
		have_key = True
		have_hanger = True
		have_note = True
	elif not(str(OPTION)=='a' or 's' or 'w' or 'd'):
		print "\n\nCOMMAND WAS INVALID!"
		ok = raw_input("\n\nCONTINUE...[Enter]")
	MOVES_REMAINING = MOVES_REMAINING - 1
	if MOVES_REMAINING == 0:
		LOSE_GAME()