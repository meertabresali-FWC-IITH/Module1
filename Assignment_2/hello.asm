;Codes for Distributive law using AVR Assembly language
;Distributive las is expressed by X.(Y+Z) = X.Y+X.Z
;LHS = X.(Y+Z), RHS = X.Y+X.Z

.include "/home/administrator/m328Pdef.inc"

	ldi r17, 0b11000111 	;identifying input pins 11,12,13 for inputs X, Y, Z
	out DDRB,r17		;declaring pins as input
	ldi r17, 0b00111001 ;
	
	out PORTB,r17		;activating internal pullup for pins 11,12,13 and assigning pin 8 for output for LHS in PORTB
	in r17,PINB

	ldi r16, 0b00000100 	;identifying output pin 2 and assignin pin 2 for RHS in PORTD
	out DDRD,r16		;declaring pins as output

;Assigning six registers; 3 forLHS and 3 for RHS
;Copying data bits from input register r17 to six registers assigned for LHS and RHS

mov r18,r17	; for X of LHS
mov r19,r17	; for Y of LHS
mov r20,r17	; for Z of LHS

mov r21,r17	; for X of RHS
mov r22,r17	; for Y of RHS
mov r23,r17 	; for Z of RHS
	
; For LHS
	
	; to shift X to 1st cell of R18

	lsr r18
	lsr r18
	lsr r18	; this is input X; 1st cell of R18

	; to shift Y to 1st cell of R19
	lsr r19
	lsr r19
	lsr r19
	lsr r19	; this is input Y; 1st cell of R19

	; to shift Z to 1st cell of R20
	lsr r20
	lsr r20
	lsr r20
	lsr r20
	lsr r20	; this is input Z; 1st cell of R20
	
	; performing operation for LHS= = X.(Y+Z)
		or r19,r20
		and r18,r19

out PORTB,r18	;writing output to pin 8 for LHS= = X.(Y+Z)

; For RHS

	lsr r21 ; this is equal to input X
	mov r24,r21

	lsr r22
	lsr r22; this is equal to Y

	lsr r23
	lsr r23
	lsr r23	;this is equal to Z
		
	; performing operation for RHS= = X.Y+X.Z
		and r21,r22
		and r24,r23
		or r21,r24

out PORTD,r21	;writing output to pin 2 for RHS= = X.Y+X.Z
	
Start:
	rjmp Start
	
