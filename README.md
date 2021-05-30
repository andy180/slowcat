# slowcat
Display a text file slowly

This is a quickly made update to the python version of slowcat by Dave W Capella at https://grox.net/software/mine/slowcat/.

This version has been updated to run in Python version 3. In this version, the delay is added to each character rather then
each line. A random change to the delay of +/-10% is applied to each character to make it look a little more like a serial
terminal from the long-lost good old days. This effect is of course more apparent with longer delays.

Run slowcat like this:

python slowcat.py -d 0.1 < thefileyouwishtoreadslowly.txt

if you make the file executable, you can omit the word 'python' from the above.



The program is copyright (c) 2002-2008 - dave w capella - All Rights Reserved
It is distributed under the terms of the GNU Public License.
It includes NO WARRANTY and NO SUPPORT.
This version as amended is Copyright (C) 2021 by Andy Middleton


This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 1, or (at your option)
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

The full GNU General Public License, version 1 may be referred to
at: https://www.gnu.org/licenses/old-licenses/gpl-1.0.html
	    

