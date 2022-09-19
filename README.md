# CRC-5-CRC-16
Calculation of 5-bit and 16-bit cyclic redundancy checks

带前缀输入校验数据（如 0b01 , 0x55ff），返回crc计算值
crc版本：
crc-5 
	参数模型 CRC-5/EPC
	宽度 5
	多项式 x^5 + x^3 + 1
	初始值 bin 01001
	校验方式 依次输入数据和校验码，结果为(bin)00000,则校验通过

crc-16
	参数模型 CRC-CCITT ？
	宽度 16
	多项式 x^16 + x^12 + x^5 + x^1
	初始值 hex ffff
	输出数据反转
	校验方式 依次输入数据和校验码，结果为(hex)1d0f,则校验通过