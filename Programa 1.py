import pyfirmata, time

led_rojo = 12
led_verde = 11
led_amarillo = 9
led_rojo1 = 8

board = pyfirmata.Arduino("COM3")
time.sleep(1)
print("Comunicacion Establecida ♥♥♥♥")
board.analog[0].mode = pyfirmata.INPUT
board.digital[led_rojo].mode = pyfirmata.OUTPUT
board.digital[led_verde].mode = pyfirmata.OUTPUT
board.digital[led_amarillo].mode = pyfirmata.OUTPUT
board.digital[led_rojo1].mode = pyfirmata.OUTPUT



iterator = pyfirmata.util.Iterator(board)
iterator.start()

while True:
        if board.analog[0].read() == None:
            pass
            
        else:
            pot = board.analog[0].read()
            print(f"Imprimiendo los datos del {pot} ☼")
            
            if pot >= 0 and pot <=0.25:
                
                board.digital[led_rojo].write(1)
                board.digital[led_verde].write(0)
                board.digital[led_amarillo].write(0)
                board.digital[led_rojo1].write(0)
                                   
            if pot >= 0.251 and pot <=0.50:
                
                
                board.digital[led_rojo].write(0)
                board.digital[led_verde].write(1)
                board.digital[led_amarillo].write(0)
                board.digital[led_rojo1].write(0)
               
                           
            if pot >= 0.501 and pot <=0.75:
                               
                board.digital[led_rojo].write(0)
                board.digital[led_verde].write(0)
                board.digital[led_amarillo].write(1)
                board.digital[led_rojo1].write(0)
                
                            
            if pot >= 0.751 and pot <=1.00:
                
                board.digital[led_rojo].write(0)
                board.digital[led_verde].write(0)
                board.digital[led_amarillo].write(0)
                board.digital[led_rojo1].write(1)
                
        
                
            