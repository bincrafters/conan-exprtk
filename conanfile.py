#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class ExprtkConan(ConanFile):
    name = "exprtk"
    version = "20181117"
    description = "ExprTk is a simple to use, easy to integrate and extremely efficient run-time mathematical expression parser and evaluation engine"
    topics = ("conan", "exprtk", "math-expressions", "parser")
    url = "https://github.com/kylemacfarlan/conan-exprtk"
    homepage = "https://github.com/ArashPartow/exprtk"
    author = "Kyle Macfarlan <kyle.macfarlan@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    no_copy_source = True

    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("http://www.partow.net/downloads/exprtk.zip", sha256="3a85058755e6d59912bb67cb1c41d9c5fd57c9ec6867fa6e73dba4a44785fac2")
        os.rename("exprtk", self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="exprtk.hpp", dst="include", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
