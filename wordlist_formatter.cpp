#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

const int MIN_WORD_LEN = 3;

bool is_valid_word(const std::string &word) {
    if (word.length() < MIN_WORD_LEN) {
        return false;
    }

    for (char c : word) {
        if (!std::isalpha(c) || !std::islower(c)) {
            return false;
        }
    }

    return true;
}

int main() {
    std::string input_filename, output_filename;

    std::cout << "Digite o nome do arquivo de word list: ";
    std::cin >> input_filename;

    std::ifstream input_file(input_filename);
    if (!input_file) {
        std::cout << "Erro ao abrir o arquivo '" << input_filename << "'\n";
        return 1;
    }

    std::cout << "Digite o nome do arquivo de saída: ";
    std::cin >> output_filename;

    std::ofstream output_file(output_filename);
    if (!output_file) {
        std::cout << "Erro ao criar o arquivo '" << output_filename << "'\n";
        return 1;
    }

    std::vector<std::string> words;
    std::string word;
    while (std::getline(input_file, word)) {
        if (is_valid_word(word)) {
            words.push_back(word);
        }
    }

    std::sort(words.begin(), words.end());
    auto last = std::unique(words.begin(), words.end());
    words.erase(last, words.end());

    for (const auto &word : words) {
        output_file << word << '\n';
    }

    std::cout << "Word list formatada com sucesso!\n";

    return 0;
}


