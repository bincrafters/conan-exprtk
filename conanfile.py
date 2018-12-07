#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from conans import ConanFile, tools


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

    def _extract_license(self, file):
        file_content = tools.load(file)
        expect = "MIT                         *"
        license_contents = file_content[2:file_content.find(expect) + len(expect)]
        tools.save(os.path.join(self.package_folder, "licenses", "LICENSE"), license_contents)

    def package(self):
        header_file = "exprtk.hpp"
        self._extract_license(os.path.join(self.source_folder, self._source_subfolder, header_file))
        self.copy(pattern=header_file, dst="include", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
