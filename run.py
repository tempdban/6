#! /usr/bin/env python
# -*- coding: utf-8 -*-

from utils import make

while True:
	s=make(raw_input(">>>").decode("utf-8"))
	if  s.sentiments > 0.6:
		print "可能是褒义"
	else:
		print "可能是贬义"