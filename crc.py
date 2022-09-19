
def to_decimal(no_decimal):
	if no_decimal[1:2]=='b':
		n=2
	elif no_decimal[1:2]=='o':
		n=8
	elif no_decimal[1:2]=='x':
		n=16
	else:
		n=10
	decimal=int(no_decimal,n)
	return decimal

def bit_len(data):
	if data[1:2]=='b':
		n=1
	elif data[1:2]=='o':
		n=3
	elif data[1:2]=='x':
		n=4
	else:
		n=0
	data_len = n*(len(data)-2)
	return data_len

def xor(m,n):
	return int(int(m)!=int(n))

def caculate_crc5(data_in):
	qn0=1
	qn1=0
	qn2=0
	qn3=1
	qn4=0
	while data_in:
		q4=qn3
		q3=xor(qn2,xor(data_in[0:1],qn4))
		q2=qn1
		q1=qn0
		q0=xor(data_in[0:1],qn4)

		qn0=q0
		qn1=q1
		qn2=q2
		qn3=q3
		qn4=q4

		data_in=data_in[1:]

	result='{}{}{}{}{}'.format(q4,q3,q2,q1,q0)
	d_result=int(result,2)
	b_result='0b' + '{:0>5}'.format(bin(d_result)[2:])
	h_result='0x' + '{:0>2}'.format(hex(d_result)[2:])
	#print(d_result)

	#print(q4,q3,q2,q1,q0)
	print('CRC-5 is:\t',b_result,'\t\t',h_result)
	if result=='00000':
		print('The CRC-5 check passes')

def caculate_crc16(data_in):
	qn0=1
	qn1=1
	qn2=1
	qn3=1
	qn4=1
	qn5=1
	qn6=1
	qn7=1
	qn8=1
	qn9=1
	qn10=1
	qn11=1
	qn12=1
	qn13=1
	qn14=1
	qn15=1

	while data_in:
		q0=xor(data_in[0:1],qn15)
		q1=qn0
		q2=qn1
		q3=qn2
		q4=qn3
		q5=xor(q0,qn4)
		q6=qn5
		q7=qn6
		q8=qn7
		q9=qn8
		q10=qn9
		q11=qn10
		q12=xor(q0,qn11)
		q13=qn12
		q14=qn13
		q15=qn14

		qn0=q0
		qn1=q1
		qn2=q2
		qn3=q3
		qn4=q4
		qn5=q5
		qn6=q6
		qn7=q7
		qn8=q8
		qn9=q9
		qn10=q10
		qn11=q11
		qn12=q12
		qn13=q13
		qn14=q14
		qn15=q15

		data_in=data_in[1:]

	result='{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(q15,q14,q13,q12,q11,\
		q10,q9,q8,q7,q6,q5,q4,q3,q2,q1,q0)
	invert_result=result.replace('0','2').replace('1','0').replace('2','1')
	d_in_result=int(invert_result,2)
	b_in_result='0b' + '{:0>16}'.format(bin(d_in_result)[2:])
	h_in_result='0x' + '{:0>4}'.format(hex(d_in_result)[2:])
	print('CRC-16 is:\t',b_in_result,'\t',h_in_result)
	if result=='0001110100001111':
		print('The CRC-16 check passes')


data_in=input('please enter data: ')
# data_in='0x0000'
data_bit_len=bit_len(data_in)
data_in=to_decimal(data_in)
data_in=bin(data_in)[2:]
data_in='{:0>{}}'.format(data_in,data_bit_len)
print('data is:\t',data_in)
caculate_crc5(data_in)
caculate_crc16(data_in)