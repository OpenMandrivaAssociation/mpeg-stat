%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	MPEG-1 video analyser
Name:		mpeg-stat
Version:	2.2b
Release:	4
License:	BSD
Group:		Video
Url:		https://bmrc.berkeley.edu/research/mpeg/
Source0:	mpeg_stat-%{version}-src.tar.gz
#http://bmrc.berkeley.edu/ftp/pub/multimedia/mpeg/stat/mpeg_stat-2.2b-src.tar.gz

%description
MPEG_STAT gathers all lot of statistics (e.g., bitrate, real Q-scale 
information, detailed motion vector/cbp information, constrained parameter 
checking, etc.).


%prep
%setup -q -n mpeg_stat

%build
%setup_compile_flags
%make mpeg_stat

%install
install -D -m 755 mpeg_stat %{buildroot}%{_bindir}/mpeg_stat
install -D -m 644 mpeg_stat.1 %{buildroot}%{_mandir}/man1/mpeg_stat.1

%files
%doc ../ANNOUNCE BUGS CHANGES COPYRIGHT README
%{_bindir}/mpeg_stat
%{_mandir}/man1/*
