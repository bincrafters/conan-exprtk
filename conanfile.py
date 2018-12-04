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
        download_url = "https://github.com/ArashPartow/exprtk"
        commit_id = "b3b4cee1c52baf935d68fe3bb7fb1a0ec6b79694"
        sha256 = "d52d50c5355bfe6edd9940b495f4bbbaa1bf51ccee9f21a1b08f8f7fdaeb577c"
        tools.get("{}/archive/{}.zip".format(download_url, commit_id), sha256=sha256)
        os.rename("{}-{}".format(self.name, commit_id), self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="exprtk.hpp", dst="include", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
