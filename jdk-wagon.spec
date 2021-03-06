#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-wagon
Version  : 2.10
Release  : 2
URL      : http://repo1.maven.org/maven2/org/apache/maven/wagon/wagon/2.10/wagon-2.10-source-release.zip
Source0  : http://repo1.maven.org/maven2/org/apache/maven/wagon/wagon/2.10/wagon-2.10-source-release.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-wagon-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-apache-resource-bundles
BuildRequires : jdk-atinject
BuildRequires : jdk-bsh
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-net
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-integration-tools
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-enforcer
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jdependency
BuildRequires : jdk-jdom
BuildRequires : jdk-jna
BuildRequires : jdk-jsch
BuildRequires : jdk-jsch-agent-proxy
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-junit4
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-artifact-resolver
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-parent
BuildRequires : jdk-maven-plugin-testing
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-remote-resources-plugin
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-exec
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-scm
BuildRequires : jdk-maven-shade-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-maven-site-plugin
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-parboiled
BuildRequires : jdk-pegdown
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-cli
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-resources
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-qdox
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Patch1: 0001-Port-to-jetty-9.patch

%description
This is a Subversion repository; use the 'svnadmin' tool to examine
it.  Do not add, delete, or modify files here unless you know how
to avoid corrupting the repository.

%package data
Summary: data components for the jdk-wagon package.
Group: Data

%description data
data components for the jdk-wagon package.


%prep
%setup -q -n wagon-2.10
%patch1 -p1

rm src/site/site.xml
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :animal-sniffer-maven-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_dep :wagon-tck-http wagon-providers/wagon-http
python3 /usr/share/java-utils/pom_editor.py pom_xpath_set      "pom:groupId[text()='org.mortbay.jetty']" "org.eclipse.jetty"
python3 /usr/share/java-utils/pom_editor.py pom_disable_module wagon-tcks
python3 /usr/share/java-utils/pom_editor.py pom_disable_module wagon-ssh-common-test wagon-providers/pom.xml
python3 /usr/share/java-utils/pom_editor.py pom_disable_module wagon-provider-test
python3 /usr/share/java-utils/pom_editor.py pom_remove_dep :wagon-provider-test
python3 /usr/share/java-utils/pom_editor.py pom_remove_dep :wagon-provider-test wagon-providers
python3 /usr/share/java-utils/pom_editor.py pom_disable_module wagon-webdav-jackrabbit wagon-providers
python3 /usr/share/java-utils/mvn_file.py ":wagon-{*}" maven-wagon/@1
python3 /usr/share/java-utils/mvn_package.py ":wagon"

%build
python3 /usr/share/java-utils/mvn_build.py -f -s; python3 /usr/share/java-utils/mvn_alias.py :wagon-http :::shaded:

%install
xmvn-install  -R .xmvn-reactor -n maven-wagon -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/maven-wagon/file.jar
/usr/share/java/maven-wagon/ftp.jar
/usr/share/java/maven-wagon/http-lightweight.jar
/usr/share/java/maven-wagon/http-shared.jar
/usr/share/java/maven-wagon/http.jar
/usr/share/java/maven-wagon/provider-api.jar
/usr/share/java/maven-wagon/scm.jar
/usr/share/java/maven-wagon/ssh-common.jar
/usr/share/java/maven-wagon/ssh-external.jar
/usr/share/java/maven-wagon/ssh.jar
/usr/share/maven-metadata/maven-wagon-wagon-file.xml
/usr/share/maven-metadata/maven-wagon-wagon-ftp.xml
/usr/share/maven-metadata/maven-wagon-wagon-http-lightweight.xml
/usr/share/maven-metadata/maven-wagon-wagon-http-shared.xml
/usr/share/maven-metadata/maven-wagon-wagon-http.xml
/usr/share/maven-metadata/maven-wagon-wagon-provider-api.xml
/usr/share/maven-metadata/maven-wagon-wagon-providers.xml
/usr/share/maven-metadata/maven-wagon-wagon-scm.xml
/usr/share/maven-metadata/maven-wagon-wagon-ssh-common.xml
/usr/share/maven-metadata/maven-wagon-wagon-ssh-external.xml
/usr/share/maven-metadata/maven-wagon-wagon-ssh.xml
/usr/share/maven-metadata/maven-wagon.xml
/usr/share/maven-poms/maven-wagon/file.pom
/usr/share/maven-poms/maven-wagon/ftp.pom
/usr/share/maven-poms/maven-wagon/http-lightweight.pom
/usr/share/maven-poms/maven-wagon/http-shared.pom
/usr/share/maven-poms/maven-wagon/http.pom
/usr/share/maven-poms/maven-wagon/provider-api.pom
/usr/share/maven-poms/maven-wagon/providers.pom
/usr/share/maven-poms/maven-wagon/scm.pom
/usr/share/maven-poms/maven-wagon/ssh-common.pom
/usr/share/maven-poms/maven-wagon/ssh-external.pom
/usr/share/maven-poms/maven-wagon/ssh.pom
/usr/share/maven-poms/maven-wagon/wagon.pom
