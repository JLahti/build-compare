#
# spec file for package build-compare (Version 2009.10.14)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           build-compare
License:        GPLv2+
Group:          Development/Tools/Building
AutoReqProv:    on
Summary:        Build Result Compare Script
Version:        2009.10.14
Release:        26
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains scripts to find out if the build result differs
to a former build.



%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/build/ $RPM_BUILD_ROOT/%_defaultdocdir/%name
install -m 0755 same-build-result.sh rpm-check.sh functions.sh srpm-check.sh $RPM_BUILD_ROOT/usr/lib/build/
install -m 0644 COPYING $RPM_BUILD_ROOT/%_defaultdocdir/%name/

%files
%defattr(-,root,root)
%doc %_defaultdocdir/%name
/usr/lib/build

%changelog
