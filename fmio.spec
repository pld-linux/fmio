Summary:	FM card initializer and FM radio player
Summary(pl):	Program inicjalizuj±cy karty radiowe
Name:		fmio
Version:	1.2.23
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://jumbo.narod.ru/src/fmio/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fm radio card manipulation utility

%description -l pl
manager kart odbieraj±cych radia nadaj±ce w FM

%prep
%setup -q

%build
%{__make}  CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/usr/share/%{name}}

install fmio $RPM_BUILD_ROOT%{_bindir}
install fmio.1 $RPM_BUILD_ROOT/%{_mandir}/man1
install *.o $RPM_BUILD_ROOT/usr/share/%{name}/

gzip -9nf Changelog README ess1868

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
/usr/share/%{name}/
