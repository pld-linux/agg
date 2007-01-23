Summary:	Anti-Grain Geometry
Name:		agg
Version:	2.5
Release:	0.1
License:	GPL
Group:		Libraries
URL:		http://www.antigrain.com/
Source0:	http://www.antigrain.com/%{name}-%{version}.tar.gz
# Source0-md5:	ddc67cbdc7d51e1ec984c2ac2724c08a
Patch0:		%{name}-depends.patch
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A High Quality Rendering Engine for C++

%package devel
Summary:	Support files necessary to compile applications with agg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries, headers, and support files necessary to compile
applications using agg

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__libtoolize}
%{__automake}
%configure \
	--disable-gpc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc authors copying readme
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_pkgconfigdir}/libagg.pc
%{_includedir}/agg2
%{_aclocaldir}/libagg.m4

%clean
rm -r $RPM_BUILD_ROOT
