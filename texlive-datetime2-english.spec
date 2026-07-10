%global tl_name datetime2-english
%global tl_revision 52479

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.05
Release:	%{tl_revision}.1
Summary:	English language module for the datetime2 package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/datetime2-contrib/datetime2-english
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-english.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-english.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-english.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This module provides the following styles that can be set using
\DTMsetstyle provided by datetime2.sty. The region not only determines
the date/time format but also the time zone abbreviations if the zone
mapping setting is on. english (English - no region) en-GB (English -
United Kingdom of Great Britain and Northern Ireland) en-US (English -
United States of America) en-CA (English - Canada) en-AU (English -
Commonwealth of Australia) en-NZ (English - New Zealand) en-GG (English
- Bailiwick of Guernsey) en-JE (English - Bailiwick of Jersey) en-IM
(English - Isle of Man) en-MT (English - Republic of Malta) en-IE
(English - Republic of Ireland)

