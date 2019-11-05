import os
from conans import ConanFile, tools


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
