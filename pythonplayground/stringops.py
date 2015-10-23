def reftest(swag,count):
	if count == 1:
		return

	swag.append(4)
	count = count - 1
	reftest(swag, count)





swag = [5]
reftest(swag, 3)

print swag