#ifndef WRITE_JSON_FILE_H
#define WRITE_JSON_FILE_H

#include <fstream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

struct MatchedAst {
    std::string type;
    std::string file;
    unsigned int line;
    unsigned int column;
};

void writeJsonFile(std::string outputJsonFile, MatchedAst info) {
    std::ifstream fileStream(outputJsonFile);
    nlohmann::json data;
    fileStream >> data;
    fileStream.close();

    data.push_back({{"file", info.file},
                    {"line", info.line},
                    {"column", info.column},
                    {"type", info.type}});

    std::ofstream outFileStream(outputJsonFile);
    outFileStream << data.dump(4);
    outFileStream.close();
}

#endif