import cv2


'''
1. Read image by path.
'''
im = cv2.imread("../rsrc/1.jpg", cv2.IMREAD_COLOR)

'''
2. Show image on the screen.
'''
cv2.imshow("my window name", im)

'''
3. Stop the program and wait the keyboard input.

key_code = cv2.waitKey( time )
--- time: 0 -> wait util key pressed.
          1000 -> only wait util key pressed in 1 second.
--- Return a key ASCII code.
'''
key_code = cv2.waitKey(0)

print("Key Code: %d" % key_code)

'''
4. More about ASCII

chr( code )
--- code: ASCII code.
--- Return a char which represent by the code.

ord( char )
--- char: only one character.
--- Return a ASCII code which represent by the character.
'''
print("The Key is %s" % chr(key_code))

print("Char 'a' => %d" % ord('a'))
