# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Constants for the configuration scoring tool."""

import enum


class FileTypes(str, enum.Enum):
  # The file which is being scored
  PROPOSED = 'proposed'
  # The file which is being compared against
  SOLUTION = 'solution'


class DimensionCategories(str, enum.Enum):
  # Receives `translations` and scores
  # only reporting entities in bulk
  SIMPLE = 'simple'
  # Receives `deserialized_files` to build a multi-map
  # of virtual entities prior to calculating scores
  COMPLEX = 'complex'