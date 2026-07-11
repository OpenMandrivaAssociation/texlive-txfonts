%global tl_name txfonts
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Times-like fonts in support of mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/txfonts
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/txfonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/txfonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Txfonts supplies virtual text roman fonts using Adobe Times (or URW
NimbusRomNo9L) with some modified and additional text symbols in the
OT1, T1, and TS1 encodings; maths alphabets using Times/URW Nimbus;
maths fonts providing all the symbols of the Computer Modern and AMS
fonts, including all the Greek capital letters from CMR; and additional
maths fonts of various other symbols. The set is complemented by a sans-
serif set of text fonts, based on Helvetica/NimbusSanL, and a monospace
set. All the fonts are in Type 1 format (AFM and PFB files), and are
supported by TeX metrics (VF and TFM files) and macros for use with
LaTeX.

