#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

void generateFrequencyVector(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Unable to open file " << filename << std::endl;
        return;
    }

    std::vector<int> frequencyVector(101, 0); // assuming values are in the range [0, 100]
    int value;

    while (true) {
        if (!(file >> value)) {
            if (file.eof()) {
                break; // end of file reached
            } else {
                std::cerr << "Invalid input in file. Skipping..." << std::endl;
                file.clear(); // clear error flag
                file.ignore(1); // skip one character
            }
        } else {
            if (value >= 0 && value <= 100) {
                frequencyVector[value]++;
            } else {
                std::cerr << "Invalid value " << value << " in file" << std::endl;
            }
        }
    }

    file.close();

    bool allValuesPresent = true;
    for (int i = 0; i <= 100; ++i) {
        if (frequencyVector[i] == 0) {
            allValuesPresent = false;
            std::cout << "Value " << i << " has not appeared at all." << std::endl;
        }
    }

    if (allValuesPresent) {
        std::cout << "All values have appeared at least once." << std::endl;
    }

    // Find the three most frequent values
    std::vector<std::pair<int, int>> valueFrequencies;
    for (int i = 0; i <= 100; ++i) {
        valueFrequencies.emplace_back(i, frequencyVector[i]);
    }

    std::sort(valueFrequencies.begin(), valueFrequencies.end(),
              [](const auto& a, const auto& b) { return a.second > b.second; });

    std::cout << "The three most frequent values are:" << std::endl;
    for (int i = 0; i < 3; ++i) {
        std::cout << "Value " << valueFrequencies[i].first << " appears " << valueFrequencies[i].second << " times." << std::endl;
    }
}

int main() {
    generateFrequencyVector("vectors.txt");
    return 0;
}
