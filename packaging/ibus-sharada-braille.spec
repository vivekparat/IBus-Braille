###########################################################################
#    ISB - IBus-sharada-braille
#    Copyright (c) 2014-2015 Nalin.x.GNU <nalin.x.linux@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################

# yum install  python3-devel
# yum install  rpm-build

Name:           ibus-braille
Version:        0.3
Release:        0%{?dist}
Epoch:          1
Summary:        ibus-braille is an ibus input engine based on six key approach of braille.

Group:          Applications/Editors
License:        GPLv3+
URL:            https://gitlab.com/smc/ibus-braille/zip/ibus-sharada-braille-0.3.zip
Source0:        https://gitlab.com/smc/ibus-braille/zip/ibus-sharada-braille-0.3.zip

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       python3-gobject
Requires:       python3-espeak
Requires:	PackageKit-gtk3-module

%description
 ibus-braille is an ibus input engine based on six key approach of braille. we express our gratitude to Swathanthra Malayalam Computing(SMC) for mentoring this project. We consider the acceptance of this project by Swathanthra Malayalam Computing and Google as a new flowering of the effort of louies braille.


%prep
%setup -q

set -e
set -x
libtoolize --automake --copy
aclocal -I m4
autoheader
automake --add-missing --copy
autoconf
export CFLAGS="-g -O0"
export CXXFLAGS="$CFLAGS"

%build
%configure --disable-static
# make -C po update-gmo
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install


#abbreviations.txt should be editable for user
chmod -R 777 $RPM_BUILD_ROOT/%{_datadir}/ibus-braille/braille/


%files
%defattr(-,root,root,-)
%{_datadir}/ibus-braille/*
%{_datadir}/ibus-braille-abbreviation-editor/*
%{_datadir}/ibus-braille-language-editor/*
%{_datadir}/ibus-braille-preferences/*
%{_datadir}/ibus/component/braille.xml
%{_datadir}/applications/*
%{_bindir}/*
