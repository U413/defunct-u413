'''u413 - an open-source BBS/terminal/PI-themed forum
	Copyright (C) 2012 PiMaster
	Copyright (C) 2012 EnKrypt

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU Affero General Public License for more details.

	You should have received a copy of the GNU Affero General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.'''

import command
import user

def prev_func(args,u413):
	context=u413.user.context.split(' ')
	if context[0]=='BOARD':
		if context[1]=='ALL':
			context[1]=0
	if context[0] in ['BOARD','TOPIC']:
		page=1
		if len(context)>2:
			page=int(context[2])
			if page>1:
				page-=1
		command.respond(context[0]+' '+str(context[1])+' '+str(page),u413)
	else:
		u413.type('"PREV" is not a valid command or is not available in the current context.')

command.Command("PREV","",{},"Goes to the previous page",prev_func,user.User.member)
