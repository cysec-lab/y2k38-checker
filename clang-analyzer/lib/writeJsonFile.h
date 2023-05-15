#ifndef WRITE_JSON_FILE_H
#define WRITE_JSON_FILE_H

#include <fstream>
#include <nlohmann/json.hpp>

#include "clang/Basic/Diagnostic.h"

using json = nlohmann::json;

struct MatchedAst {
    llvm::StringRef file;
    std::string type;
    int line;
    int column;
};

void writeJsonFile(MatchedAst info) {
    std::string outputJson = "output.json";
    std::ifstream fileStream(outputJson);
    nlohmann::json data;
    fileStream >> data;
    fileStream.close();

    data.push_back({{"file", info.file},
                    {"line", info.line},
                    {"column", info.column},
                    {"type", info.type}});

    std::ofstream outFileStream(outputJson);
    outFileStream << data.dump(4);
    outFileStream.close();
}

#endif