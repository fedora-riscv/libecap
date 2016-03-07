Name:       libecap
Version:    1.0.0
Release:    1%{?dist}
Summary:    Squid interface for embedded adaptation modules
License:    BSD
Group:      Development/Libraries
URL:        http://www.e-cap.org/
Source0:    http://www.measurement-factory.com/tmp/ecap/%{name}-%{version}.tar.gz
Source1:    autoconf.h

%description
eCAP is a software interface that allows a network application, such as an 
HTTP proxy or an ICAP server, to outsource content analysis and adaptation to 
a loadable module. For each applicable protocol message being processed, an 
eCAP-enabled host application supplies the message details to the adaptation 
module and gets back an adapted message, a "not interested" response, or a 
"block this message now!" instruction. These exchanges often include message 
bodies.

The adaptation module can also exchange meta-information with the host 
application to supply additional details such as configuration options, a 
reason behind the decision to ignore a message, or a detected virus name.

If you are familiar with the ICAP protocol (RFC 3507), then you may think of 
eCAP as an "embedded ICAP", where network interactions with an ICAP server are 
replaced with function calls to an adaptation module.

%package devel
Summary:    Libraries and header files for the libecap library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package provides the libraries, include files, and other
resources needed for developing libecap applications.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libecap.a
rm -f %{buildroot}%{_libdir}/libecap.la

# Rename libecap/common/autoconf.h to libecap/common/autoconf-<arch>.h to avoid file conflicts on
# multilib systems and install autoconf.h wrapper
mv %{buildroot}%{_includedir}/%{name}/common/autoconf.h %{buildroot}%{_includedir}/%{name}/common/autoconf-%{_arch}.h
install -m644 %{SOURCE1} %{buildroot}%{_includedir}/%{name}/common/autoconf.h

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc LICENSE CREDITS NOTICE README
%{_libdir}/libecap.so.*

%files devel
%{_libdir}/libecap.so
%{_libdir}/pkgconfig/libecap.pc
%{_includedir}/libecap

%changelog
* Mon Mar 07 2016 Luboš Uhliarik <luhliari@redhat.com> - 1.0.0-1
- new version 1.0.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jaromir Capik <jcapik@redhat.com> - 0.2.0-8
- Introducing suppport for ppc64le in autoconf.h (#1075180)

* Mon Sep 16 2013 Michal Luscon <mluscon@redhat.com> - 0.2.0-7
- Fixed: #831404 - multilib conflicts due to platform dependent autoconf.h

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Chris Spike <spike@fedoraproject.org> 0.2.0-2
- Added pkgconfig file to -devel

* Mon Jul 11 2011 Chris Spike <spike@fedoraproject.org> 0.2.0-1
- Updated to 0.2.0

* Tue May 10 2011 Chris Spike <spike@fedoraproject.org> 0.0.3-2
- Added LICENSE to doc
- Fixed release tag (missing dist)

* Wed Apr 27 2011 Chris Spike <spike@fedoraproject.org> 0.0.3-1
- Initial version of the package
