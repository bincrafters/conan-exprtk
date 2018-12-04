#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class ExprtkConan(ConanFile):
    name = "exprtk"
    version = "20181202"
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
        commit_id = "88acc921e28d9e80b0c61663257bd8ff7997bcb8"
        sha256 = "430829a20b469cb584d75815cee2c693dda2feac6e63c407d17029d5cf5e26e9"
        tools.get("{}/archive/{}.zip".format(download_url, commit_id), sha256=sha256)
        os.rename("{}-{}".format(self.name, commit_id), self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="exprtk.hpp", dst="include", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
