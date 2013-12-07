# revision 15878
# category Package
# catalog-ctan /fonts/txfonts
# catalog-date 2009-01-15 09:33:18 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-txfonts
Version:	20090115
Release:	3
Summary:	Times-like fonts in support of mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/txfonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txfonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txfonts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Txfonts supplies virtual text roman fonts using Adobe Times (or
URW NimbusRomNo9L) with some modified and additional text
symbols in the OT1, T1, and TS1 encodings; maths alphabets
using Times/URW Nimbus; maths fonts providing all the symbols
of the Computer Modern and AMS fonts, including all the Greek
capital letters from CMR; and additional maths fonts of various
other symbols. The set is complemented by a sans-serif set of
text fonts, based on Helvetica/NimbusSanL, and a monospace set.
All the fonts are in Type 1 format (AFM and PFB files), and are
supported by TeX metrics (VF and TFM files) and macros for use
with LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxb.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxbi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxbss.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxr.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtcxss.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxb.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxbi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxbmi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxbsc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxbss.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxbsssc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxmi.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxr.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxsc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxss.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/rtxsssc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/t1xbtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/t1xbttsc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/t1xtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/t1xttsc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/tcxbtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/tcxtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbex.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbexa.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbmia.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbsy.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbsya.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbsyb.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbsyc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txbttsc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txex.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txexa.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txmia.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txsy.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txsya.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txsyb.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txsyc.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txtt.afm
%{_texmfdistdir}/fonts/afm/public/txfonts/txttsc.afm
%{_texmfdistdir}/fonts/enc/dvips/txfonts/tx8r.enc
%{_texmfdistdir}/fonts/map/dvips/txfonts/txfonts.map
%{_texmfdistdir}/fonts/map/dvips/txfonts/txr.map
%{_texmfdistdir}/fonts/map/dvips/txfonts/txr1.map
%{_texmfdistdir}/fonts/map/dvips/txfonts/txr2.map
%{_texmfdistdir}/fonts/map/dvips/txfonts/txr3.map
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxbsso.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtcxsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxbsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxmi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxphvb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxphvbo.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxphvr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxphvro.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmbo.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmri.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxptmro.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/rtxsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xbttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/t1xttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxbttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tcxttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbex.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbexa.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbmia.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsy.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsya.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txbttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txex.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txexa.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txmi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txmi1.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txmia.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsy.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsya.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsyb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txsyc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/txttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxb.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxbttsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxi.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxr.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxsl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxss.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxsssc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxsssl.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxtt.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxttsc.tfm
%{_texmfdistdir}/fonts/tfm/public/txfonts/tyxttsl.tfm
%{_texmfdistdir}/fonts/type1/public/txfonts/rtcxb.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtcxbi.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtcxbss.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtcxi.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtcxr.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtcxss.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxb.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxbi.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxbmi.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxbsc.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxbss.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxbsssc.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxi.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxmi.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxr.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxsc.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxss.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/rtxsssc.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/t1xbtt.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/t1xbttsc.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/t1xtt.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/t1xttsc.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/tcxbtt.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/tcxtt.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txbex.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txbexa.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txbmia.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txbsy.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txbsya.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txbsyb.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txbsyc.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txbtt.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txbttsc.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txex.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txexa.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txmia.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txsy.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txsya.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txsyb.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txsyc.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txtt.pfb
%{_texmfdistdir}/fonts/type1/public/txfonts/txttsc.pfb
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xb.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xbsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xr.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/t1xsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxb.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxbi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxbsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxbss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxbsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxr.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tcxsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txb.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbmi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbmi1.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txbsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txmi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txmi1.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txr.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/txsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxb.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbtt.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbttsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxbttsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxi.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxr.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxsl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxss.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxsssc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxsssl.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxtt.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxttsc.vf
%{_texmfdistdir}/fonts/vf/public/txfonts/tyxttsl.vf
%{_texmfdistdir}/tex/latex/txfonts/ly1txr.fd
%{_texmfdistdir}/tex/latex/txfonts/ly1txss.fd
%{_texmfdistdir}/tex/latex/txfonts/ly1txtt.fd
%{_texmfdistdir}/tex/latex/txfonts/omltxmi.fd
%{_texmfdistdir}/tex/latex/txfonts/omltxr.fd
%{_texmfdistdir}/tex/latex/txfonts/omstxr.fd
%{_texmfdistdir}/tex/latex/txfonts/omstxsy.fd
%{_texmfdistdir}/tex/latex/txfonts/omxtxex.fd
%{_texmfdistdir}/tex/latex/txfonts/ot1txr.fd
%{_texmfdistdir}/tex/latex/txfonts/ot1txss.fd
%{_texmfdistdir}/tex/latex/txfonts/ot1txtt.fd
%{_texmfdistdir}/tex/latex/txfonts/t1txr.fd
%{_texmfdistdir}/tex/latex/txfonts/t1txss.fd
%{_texmfdistdir}/tex/latex/txfonts/t1txtt.fd
%{_texmfdistdir}/tex/latex/txfonts/ts1txr.fd
%{_texmfdistdir}/tex/latex/txfonts/ts1txss.fd
%{_texmfdistdir}/tex/latex/txfonts/ts1txtt.fd
%{_texmfdistdir}/tex/latex/txfonts/txfonts.sty
%{_texmfdistdir}/tex/latex/txfonts/utxexa.fd
%{_texmfdistdir}/tex/latex/txfonts/utxmia.fd
%{_texmfdistdir}/tex/latex/txfonts/utxr.fd
%{_texmfdistdir}/tex/latex/txfonts/utxss.fd
%{_texmfdistdir}/tex/latex/txfonts/utxsya.fd
%{_texmfdistdir}/tex/latex/txfonts/utxsyb.fd
%{_texmfdistdir}/tex/latex/txfonts/utxsyc.fd
%{_texmfdistdir}/tex/latex/txfonts/utxtt.fd
%doc %{_texmfdistdir}/doc/fonts/txfonts/00bug_fix.txt
%doc %{_texmfdistdir}/doc/fonts/txfonts/COPYRIGHT
%doc %{_texmfdistdir}/doc/fonts/txfonts/README
%doc %{_texmfdistdir}/doc/fonts/txfonts/txfontsdoc.pdf
%doc %{_texmfdistdir}/doc/fonts/txfonts/txfontsdoc.tex
%doc %{_texmfdistdir}/doc/fonts/txfonts/txfontsdocA4.pdf
%doc %{_texmfdistdir}/doc/fonts/txfonts/txfontsdocA4.tex
%doc %{_texmfdistdir}/doc/fonts/txfonts/txmi.vpl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090115-2
+ Revision: 757162
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090115-1
+ Revision: 719821
- texlive-txfonts
- texlive-txfonts
- texlive-txfonts

