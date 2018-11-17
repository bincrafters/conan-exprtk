#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class ExprtkConan(ConanFile):
    name = "exprtk"
    version = "20181117"
    url = "https://github.com/kylemacfarlan/conan-exprtk"
    author = "Kyle Macfarlan <kyle.macfarlan@gmail.com>"
    description = "ExprTk is a simple to use, easy to integrate and extremely efficient run-time mathematical expression parser and evaluation engine"
    no_copy_source = True

    # Indicates License type of the packaged library
    license = "MIT"

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"

    def source(self):
        tools.get("http://www.partow.net/downloads/exprtk.zip")

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename("exprtk", self.source_subfolder)


    def package(self):
        include_folder = self.source_subfolder
        self.copy(pattern="LICENSE", dst="license", src=self.source_subfolder)
        self.copy(pattern="exprtk.hpp", dst="include", src=include_folder)


    def package_id(self):
        self.info.header_only()
