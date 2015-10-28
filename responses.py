def emailResopnses(bodyText):
	rot = "rotate"
	position = "position"
	rotToPos="rotate to postion number"
	resetTime="Reset Time"
	fuckYou = "Well fuck you too kid"
	notFound = "You have entered an unknowm command. The only proper commands are [fill this out later]"

	if rot in bodyText:
		return rot
	elif position in bodyText:
		return position
	elif rotToPos in bodyText:
		return rotToPos
	elif resetTime in bodyText:
		return resetTime
	elif fuckYou in bodyText:
		return fuckYou
	else:
		return notFound




