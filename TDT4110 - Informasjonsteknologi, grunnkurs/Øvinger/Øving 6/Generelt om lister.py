__author__ = 'Niklas'
# -*- coding: utf-8 -*-


   ###    ###
  ## ##     ##
 ##   ##     ##
##     ##    ##
#########    ##
##     ##   ##
##     ## ###

li = list(range(1, 7))


########  ###
##     ##   ##
##     ##    ##
########     ##
##     ##    ##
##     ##   ##
########  ###

li = [i*-1 for i in li]


 ######  ###
##    ##   ##
##          ##
##          ##
##          ##
##    ##   ##
 ######  ###

li = li[::-1]
# Kan også bruke li = li.reversed()


########  ###
##     ##   ##
##     ##    ##
##     ##    ##
##     ##    ##
##     ##   ##
########  ###

print(li)
