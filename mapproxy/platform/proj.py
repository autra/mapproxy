# This file is part of the MapProxy project.
# Copyright (C) 2010 Omniscale <http://omniscale.de>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import platform

__all__ = ['Proj', 'transform', 'set_datapath', 'ProjInitError']

if platform.system() == "Java":
    from mapproxy.platform.jython.proj import (
        Proj, transform, set_datapath, ProjInitError
    )
    Proj, transform, set_datapath, ProjInitError # prevent pyflake warnings
else:
    from mapproxy.platform.cpython.proj import (
        Proj, transform, set_datapath, ProjInitError
    )
