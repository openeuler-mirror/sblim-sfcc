Name: sblim-sfcc
Summary: Small Footprint CIM Client Library
Version: 2.2.8
Release: 11
License: EPL
URL: http://www.sblim.org
Source0: http://downloads.sourceforge.net/project/sblim/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: libcurl-devel gcc chrpath gcc-c++

%Description
The small footprint CIM client library is a C API allowing client applications
to interface with CIM implementations (e.g. CIM servers). Due to it's small
memory and disk footprint it is well-suited for embedded environments.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%Description devel
%{name} Library Header Files and Link Libraries

%package_help

%prep

%autosetup -p1

%build
chmod a-x backend/cimxml/*.[ch]

%configure
%make_build

%install
make DESTDIR=%{buildroot} install
chrpath --delete %{buildroot}%{_libdir}/libcmpisfcc.so.1.0.0

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*
%{_libdir}/libcimcClientXML.so
%exclude %{_libdir}/*a

%files devel
%{_includedir}/cimc/*
%{_includedir}/CimClientLib/*
%{_libdir}/libcmpisfcc.so
%{_libdir}/libcimcclient.so

%files help
%{_docdir}/*
%{_mandir}/man3/*.3.gz

%changelog
* Tue Nov 19 2019 caomeng<caomeng5@huawei.com> - 2.2.8 -11
- Package init
