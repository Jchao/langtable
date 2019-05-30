Name:           langtable
Version:        0.0.44
Release:        1%{?dist}
Summary:        Guessing reasonable defaults for locale, keyboard layout, territory, and language.
# the translations in languages.xml and territories.xml are (mostly)
# imported from CLDR and are thus under the Unicode license, the
# short name for this license is "MIT", see:
# https://fedoraproject.org/wiki/Licensing:MIT?rd=Licensing/MIT#Modern_Style_without_sublicense_.28Unicode.29
License:        GPLv3+
URL:            https://github.com/mike-fabian/langtable
Source0:        https://github.com/mike-fabian/langtable/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  python3-devel

%description
langtable is used to guess reasonable defaults for locale, keyboard layout,
territory, and language, if part of that information is already known. For
example, guess the territory and the keyboard layout if the language
is known or guess the language and keyboard layout if the territory is
already known.

%package -n python3-langtable
Summary:        Python module to query the langtable-data
License:        GPLv3+
Requires:       %{name} = %{version}-%{release}

%description -n python3-langtable
This package contains a Python module to query the data
from langtable-data.

%prep
%setup -q

%build
perl -pi -e "s,_DATADIR = '(.*)',_DATADIR = '%{_datadir}/langtable'," langtable/langtable.py

%py3_build

%install

%py3_install

%check
(cd $RPM_BUILD_DIR/%{name}-%{version}/langtable; %{__python3} langtable.py)
(cd $RPM_BUILD_DIR/%{name}-%{version}; %{__python3} test_cases.py)
xmllint --noout --relaxng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/schemas/keyboards.rng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/data/keyboards.xml.gz
xmllint --noout --relaxng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/schemas/languages.rng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/data/languages.xml.gz
xmllint --noout --relaxng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/schemas/territories.rng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/data/territories.xml.gz
xmllint --noout --relaxng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/schemas/timezoneidparts.rng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/data/timezoneidparts.xml.gz
xmllint --noout --relaxng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/schemas/timezones.rng \
        $RPM_BUILD_DIR/%{name}-%{version}/langtable/data/timezones.xml.gz

%files
%license COPYING unicode-license.txt
%doc README ChangeLog test_cases.py langtable/schemas/*.rng

%files -n python3-langtable
%dir %{python3_sitelib}/langtable
%{python3_sitelib}/langtable/*
%dir %{python3_sitelib}/langtable-*.egg-info
%{python3_sitelib}/langtable-*.egg-info/*

%changelog
* Fri May 31 2019 Mike FABIAN <mfabian@redhat.com> - 0.0.44-1
- Use setuptools instead of distutils
- Add a version() function and an info() function.
- Restructure langtable project a bit to be able to upload to PyPi
- Increase the rank of zh_SG.UTF-8 back to 10 again for languageId="zh"
- Remove old provides and obsoletes

* Fri May 10 2019 Mike FABIAN <mfabian@redhat.com> - 0.0.43-1
- Get translation changes from CLDR
- Add some new translations from CLDR
- Add dsb_DE.UTF-8 sah_RU.UTF-8 locales
- Fix ranks for "en" and "zh" in "SG", English should be the default for "SG"
- Reduce the rank of cmn_TW.UTF-8 and zh_SG.UTF-8 to 0 for languageId="zh"
  (Resolves: https://github.com/mike-fabian/langtable/issues/8)

* Mon Apr 08 2019 Mike FABIAN <mfabian@redhat.com> - 0.0.42-1
- Add special support for languageId ca_ES_VALENCIA (Resolves: rhbz#1698984)

* Fri Mar 08 2019 Mike FABIAN <mfabian@redhat.com> - 0.0.41-3
- Remove python2-langtable subpackage (Resolves: rhbz#1686395)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Mike FABIAN <mfabian@redhat.com> - 0.0.41-1
- The territory can be 2 upper case letters *or* 3 digits
- Get translation changes from CLDR
- Add many languages and territories and also add new translations from CLDR

* Mon Jan 07 2019 Mike FABIAN <mfabian@redhat.com> - 0.0.40-1
- Add Esperanto locale and test case
  (Thanks to Carmen Bianca Bakker <carmen@carmenbianca.eu>).
- Add sel

* Thu Nov 08 2018 Mike FABIAN <mfabian@redhat.com> - 0.0.39-2
- Remove unnecessary LC_CTYPE=en_US.UTF-8 in check section.

* Mon Oct 15 2018 Mike FABIAN <mfabian@redhat.com> - 0.0.39-1
- Add the new keyboard layout "au" for Australia (same as "us")
- Add locales missing in languages.xml, territiories.xml or in both.
- Add ibus/libzhuyin and make it the default for TW.
- Add cmn_TW.UTF-8 to the Chinese locales
- Add several missing  languages (Resolves: rhbz#1631214):
  ab av bin bm bua ch co cu ee fat gn ho hz ie ii io kaa ki kj kr kum
  kwm lah lez mh mo na ng nqo nv ota rm rn sco sg sh sma smn sms sn su
  syr tw ty tyv vo vot wen yap za

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.38-8
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.38-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.38-6
- Rebuilt for Python 3.7

* Tue Apr 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0.0.38-5
- Conditionally add back Python 2 subpackage on Fedora
- Rename Python 3 subpackage to python3-langtable to follow guidelines
- Resolves: rhbz#1559099

* Wed Apr 04 2018 Mike FABIAN <mfabian@redhat.com> - 0.0.38-4
- Drop Python 2 subpackage
- Resolves: rhbz#1559099

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 06 2017 Mike FABIAN <mfabian@redhat.com> - 0.0.38-2
- Make "tw" the default keyboard layout for zh_TW and cmn_TW
- Resolves: rhbz#1387825

* Mon Nov 06 2017 Mike FABIAN <mfabian@redhat.com> - 0.0.38-1
- Add some new translations from CLDR
- Add agr, bi, hif, kab, mfe, miq, mjw, shn, sm, to, tpi_PG, yuw, AS, MU, SC, TO, VU, WS

* Wed Sep 27 2017 Troy Dawson <tdawson@redhat.com> - 0.0.37-4
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.0.37-3
- Python 2 binary package renamed to python2-langtable
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 08 2017 Mike FABIAN <mfabian@redhat.com> - 0.0.37-1
- Add some new translations from CLDR
- Add sgs
- Add chr
- Add Hung script

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.0.36-3
- Rebuild for Python 3.6

* Thu Jul 21 2016 Mike FABIAN <mfabian@redhat.com> - 0.0.36-2
- add BuildRequires: perl

* Wed Jul 20 2016 Mike FABIAN <mfabian@redhat.com> - 0.0.36-1
- Add LI (a de_LI locale has recently been added to glibc)
- Add some translations for LI from CLDR

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.35-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 24 2016 Mike FABIAN <mfabian@redhat.com> - 0.0.35-1
- Add some translations from CLDR
- Translation fix for Cyprus in Turkish (Resolves: rhbz#1349245)
- Fix script entries for ID and BA
- Add khb, osa, new, xzh and Bhks and Marc scripts

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Feb 3 2016 Orion Poplawski <orion@cora.nwra.com> - 0.0.34-3
- Modernize spec
- Fix python3 package file ownership

* Tue Nov 03 2015 Robert Kuska <rkuska@redhat.com> - 0.0.34-2
- Rebuilt for Python3.5 rebuild

* Wed Jul 01 2015 Mike FABIAN <mfabian@redhat.com> - 0.0.34-1
- Add a function list_scripts() to list scripts used for a language or in a territory
- Translation fix from CLDR
- Add Sphinx markup to public functions

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Mike FABIAN <mfabian@redhat.com> - 0.0.33-1
- Translation fix for Tagalog <-> Filipino
- Resolves: rhbz#1220775
- Translation fixes from Wikipedia and CLDR
- fix build with Python 3.4.3 (in current rawhide)

* Tue May 12 2015 Mike FABIAN <mfabian@redhat.com> - 0.0.32-1
- Add language endonym for tl
- Resolves: rhbz#1220783

* Tue Apr 28 2015 Mike FABIAN <mfabian@redhat.com> - 0.0.31-2
- Do not package the files in /usr/share/langtable/ twice
- Resolves: rhbz#1216913

* Thu Mar 05 2015 Mike FABIAN <mfabian@redhat.com> - 0.0.31-1
- Fix keyboard for sr_ME ('rs', not 'sr'), by David Shea (Resolves: rhbz#1190078)
- Add tcy and bhb
- Add some new translations from CLDR
- Some translation fixes  from CLDR

* Tue Jan 27 2015 Mike FABIAN <mfabian@redhat.com> - 0.0.30-1
- Make “eurlatgr” the default console font for languages and regions which
  do not need Arabic or Cyrillic or Hebrew script.
- add ce, raj

* Wed Jan 14 2015 Mike FABIAN <mfabian@redhat.com> - 0.0.29-1
- add CW, cmn, hak, lzh, quz, the

* Wed Sep 24 2014 Mike FABIAN <mfabian@redhat.com> - 0.0.28-1
- Do not used translations tagged with 'variant' in CLDR
- Rename Uyghur keyboard cn(uig) → cn(ug)
  (for xkeyboard-config >= 2.12, shipped with Fedora 21 Alpha)

* Wed Aug 27 2014 Mike FABIAN <mfabian@redhat.com> - 0.0.27-1
- Use Hindi again as the default language for India (Resolves: rhbz#1133188)
- Some translation updates from CLDR.

* Mon Aug 25 2014 Mike FABIAN <mfabian@redhat.com> - 0.0.26-1
- Use English as the default language for India (Resolves: rhbz#1133188)

* Wed Jul 09 2014 Mike FABIAN <mfabian@redhat.com> - 0.0.25-1
- Add fi(classic) keyboard layout (Resolves: rhbz#1117860)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu May 22 2014 Mike FABIAN <mfabian@redhat.com> - 0.0.24-2
- Resolves: rhbz#1100230 - Unowned dir /usr/share/langtable

* Mon Feb 24 2014 Mike FABIAN <mfabian@redhat.com> - 0.0.24-1
- mark Bengali (bd) and its Probhat variant layout as not ASCII-capable (by Adam Williamson)
- Also validate timezones.xml and timezoneidparts.xml in .spec file
- List list_inputmethods() as public API
- Fall back to returning untranslated timezone id if translation for the requested language does not exist (Resolves: rhbz#1032848)

* Tue Dec 10 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.23-1
- Change English translation for or from “Oriya” to “Odia” (Resolves: rhbz#1039496)
- Some new translations and translation fixes from CLDR

* Wed Dec 04 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.22-1
- Fix typo in territory and locale for ms (Resolves: rhbz#1038109)
- add ba, chm, kv, sah, syc, udm, xal
- add entries for more keyboard layouts known to be non-ASCII

* Thu Nov 21 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.21-1
- Make America/New_York the highest ranked timezone for US and yi (Resolves: rhbz#1031319)

* Wed Nov 20 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.20-1
- add entries for several layouts known to be non-ASCII by systemd/s-c-k (patch by Adam Williamson)

* Mon Nov 11 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.19-1
- Add SS
- More translations for anp from CLDR
- Add information about default input methods and a query function

* Mon Nov 04 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.18-1
- Add anp
- Do not fail if a timezone id part cannot be found in the database (Vratislav Podzimek reported that error)

* Tue Oct 22 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.17-1
- Add “be(oss)” as a possible keyboard layout for language nl (Resolves: rhbz#885345)

* Tue Oct 08 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.16-1
- Make it work with python3 (and keep it working with python2) (Resolves: rhbz#985317)

* Mon Sep 16 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.15-1
- Update to 0.0.15
- Add keyboards "ara", "ara(azerty)", "iq", and "sy" (Resolves: rhbz#1008389)

* Sun Sep 15 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.14-1
- Update to 0.0.14
- add some more languages: ay, ayc, ayr, niu, szl, nhn
- make languageId() work even if the name of the language or the territory contain spaces (Resolves: rhbz#1006718)
- Add the default script if not specified in queries for Chinese
- Import improved translations from CLDR
- Always return the territory name as well if queried in language_name()
- Add timezones.xml and timezoneidparts.xml to be able to offer translations for timezone ids
- Import translations for timezone cities from CLDR
- Add some more territories and translations
- test cases for timezone id translations

* Thu Sep 05 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.13-1
- Update to 0.0.13
- Serbian keyboards are 'rs' not 'sr' (by Vratislav Podzimek)

* Wed Aug 28 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.12-1
- Update to 0.0.12
- Match case insensitively in languageId() (Resolves: rhbz#1002000 (case insensitive languageId function needed))

* Mon Aug 19 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.11-1
- Update to 0.0.11
- Add translations for DE and NL territories in nds (reported by Vratislav Podzimek)

* Tue Aug 13 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.10-1
- Update to 0.0.10
- Add translations for Belarusian and Belarus in Latin script (reported by Vratislav Podzimek)

* Sat Aug 03 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.9-1
- Update to 0.0.9
- Add endonyms for pa_Arab (and pa_PK) and translation of country name for Pakistan for pa_Arab
- make languageId() return something even if a language name like "language (territory)" is given (Resolves: rhbz#986659 - some language name to its locale code failed)

* Tue Jul 30 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.8-1
- Update to 0.0.8
- Add endonym for Maithili
- Return True by default from supports_ascii (by Vratislav Podzimek)
- Add grc, eo, ak, GH, cop, dsb, fj, FJ, haw, hil, la, VA, ln, kg, CD, CG, AO, mos, BF, ny, MW, smj, tet, TL, tpi, PG (Resolves: rhbz#985332 - some language codes are missing)
- Import more translations from CLDR
- Give pa_IN.UTF-8 higher weight than pa_PK.UTF-8 (Resolves: rhbz#986658, rhbz#986155)

* Thu Jul 04 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.7-1
- Update to 0.0.7
- Add examples for list_consolefonts()
- Add a list_timezones() function
- Add functions languageId() and territoryId()
- Fix some translations of language names to get unique results returned by languageId()

* Wed Jun 12 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.6-1
- Update to 0.0.6
- Add RelaxNG schemas for the XML files (Vratislav Podzimek <vpodzime@redhat.com>)
- Use SAX instead of the ElementTree (Vratislav Podzimek <vpodzime@redhat.com>)
- Use 'trName' instead of 'name' for translated names (Vratislav Podzimek <vpodzime@redhat.com>)

* Fri Jun 07 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.5-1
- Update to 0.0.5
- Accept script names as used by glibc locales as well
- Support reading gzipped xml files
- Set ASCII support to “True” for cz and sk keyboard layouts

* Mon May 27 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.4-1
- Update to 0.0.4
- Remove backwards compatibility init() function
- Add ia (Interlingua), see https://bugzilla.redhat.com/show_bug.cgi?id=872423

* Thu May 16 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.3-1
- Update to 0.0.3
- Move the examples from the README to the source code
- Some tweaks for the translation of Serbian
- Prefix all global functions and global variables which are internal with “_”
- Rename country → territory, countries → territories in keyboards.xml
- Add keyboard “in(eng)” and make it the default for all Indian languages
- Add a comment stating which functions should be considered public API
- Add a supports_ascii() function
- Run Python’s doctest also on langtable.py, not only the extra test_cases.txt

* Fri May 10 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.2-1
- update to 0.0.2
- Prefer values for language, script, and territory found in languageId over those found in the other parameters

* Tue May 07 2013 Mike FABIAN <mfabian@redhat.com> - 0.0.1-1
- initial package



