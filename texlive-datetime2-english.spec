Name:		texlive-datetime2-english
Version:	52479
Release:	1
Summary:	English language module for the datetime2 package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datetime2-english
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-english.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-english.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-english.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This module provides the following styles that can be set using
\DTMsetstyle provided by datetime2.sty. The region not only
determines the date/time format but also the time zone
abbreviations if the zone mapping setting is on. english
(English - no region) en-GB (English - United Kingdom of Great
Britain and Northern Ireland) en-US (English - United States of
America) en-CA (English - Canada) en-AU (English - Commonwealth
of Australia) en-NZ (English - New Zealand) en-GG (English -
Bailiwick of Guernsey) en-JE (English - Bailiwick of Jersey)
en-IM (English - Isle of Man) en-MT (English - Republic of
Malta) en-IE (English - Republic of Ireland)

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/datetime2-english
%{_texmfdistdir}/tex/latex/datetime2-english
%doc %{_texmfdistdir}/doc/latex/datetime2-english

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
