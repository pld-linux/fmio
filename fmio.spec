Summary:	FM card initializer and FM radio player
Summary(pl):	Program inicjalizuj±cy karty radiowe
Name:		fmio
Version:	1.2.29
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://jumbo.narod.ru/src/fmio/%{name}-%{version}.tar.gz
Patch0:		%{name}-etc_dir.patch
URL:		http://jumbo.narod.ru/fmio.html
ExclusiveArch:	%{ix86} alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fm radio card manipulation utility.

%description -l pl
Program zarz±dzaj±cy kart± radiow± FM.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CC="%{__cc} %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}}

install fmio $RPM_BUILD_ROOT%{_bindir}
install fmio.1 $RPM_BUILD_ROOT%{_mandir}/man1
install *.o $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README ess1868
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
