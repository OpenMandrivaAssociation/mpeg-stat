Name: 	 		mpeg-stat
Version: 		2.2b
Release:		%mkrel 1

Summary: 	MPEG-1 video analyser
Source0: 	mpeg_stat-%{version}-src.tar.gz
#http://bmrc.berkeley.edu/ftp/pub/multimedia/mpeg/stat/mpeg_stat-2.2b-src.tar.gz
License: 	BSD
Group:	 	Video
BuildRoot: 	%{_tmppath}/%{name}-%{version}
URL:		http://bmrc.berkeley.edu/research/mpeg/

%description
MPEG_STAT gathers all lot of statistics (e.g., bitrate, real Q-scale 
information, detailed motion vector/cbp information, constrained parameter 
checking, etc.).


%prep
%setup -q -n mpeg_stat

%build
%make mpeg_stat

%install
rm -rf %{buildroot}
install -D -m 755 mpeg_stat %{buildroot}%{_bindir}/mpeg_stat
install -D -m 644 mpeg_stat.1 %{buildroot}%{_mandir}/man1/mpeg_stat.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ../ANNOUNCE BUGS CHANGES COPYRIGHT README
%{_bindir}/mpeg_stat
%{_mandir}/man1/*

