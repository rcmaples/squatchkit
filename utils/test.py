# Python 3

# Super simple, use CamelCase when
# bulding components with this script.
# Use PascalCase when naming your component.
# ex: `yarn nc MyComponent`

import sys
import os
from string import Template

# early out if args don't match expectations
# (i.e. more than 1 or less than 1 argument)
if len(sys.argv) != 2:
    print('must provide exactly one component name:\n `yarn nc MyComponent`')
    sys.exit()

component_name = sys.argv[1]

# exit if component name isn't Capitalized
if not component_name[0].isupper():
    print("components must start with a capital letter: ex: MyComponent")
    sys.exit()

parent_dir = f"{os.getcwd()}/src/components"
main_styles_dir = f"{os.getcwd()}/src/styles"
comp_dir = f"{parent_dir}/{component_name}"

# early out if component with same name exists
if os.path.exists(comp_dir):
    print(
        f"Component `{component_name}` already exists. Please choose a different name."
    )
    sys.exit()


# Test Boilerplate
def create_test(comp):
    test_dir = f"{comp_dir}/__tests__"
    test_file = f"{comp}.test.tsx"

    os.mkdir(test_dir)

    test_file_writer = open(f"{test_dir}/{test_file}", "w+")
    t = Template("""import { render, screen } from '@testing-library/react';
import { $comp } from '../index'
describe("<$comp />", () => {
    // write tests
})\n""")
    test_file_writer.write(t.substitute({'comp': comp}))
    test_file_writer.close()
    return


# Styles Boilerplate
def create_styles(comp):
    # Create the scss stub
    styles_file = f"_{comp}.scss"
    styles_file_writer = open(f"{comp_dir}/{styles_file}", "w+")
    t = """@import '../../styles/base/colors';
@import '../../styles/base/global';
@import '../../styles/base/typeface';
@import '../../styles/base/variables';"""

    styles_file_writer.write(t)
    styles_file_writer.close()

    # Link the partial to the primary styles.scss
    main_styles = open(main_styles_dir + "/" + "styles.scss", "a")
    main_styles.write(f"\n@import '../components/{comp}/{comp}';")
    main_styles.close()
    return


# Component Boilerplate
def create_component(comp):
    comp_file = f"{comp}.tsx"
    comp_file_writer = open(f"{comp_dir}/{comp_file}", "w+")
    t = Template("""import React from 'react';
export interface $prop_str {
    children?: any;
}

export const $comp: React.FC<$prop_str> = () => {
    return (<$comp />);
}; """)
    comp_file_writer.write(
        t.substitute({
            'prop_str': f"{comp}Props",
            'comp': comp
        }))
    comp_file_writer.close()
    return


# Storybook Boilerplate
def create_story(comp):
    story_file = f"{comp}.stories.tsx"
    story_file_writer = open(f"{comp_dir}/{story_file}", "w+")
    t = Template("""// import React from 'react';
import { Meta } from '@storybook/react/types-6-0';
import { Story } from '@storybook/react';
import { $comp, $prop_str } from './$comp';

export default { ...rest } as Meta;
const Template: Story<$prop_str> = (args) => <$comp {...args} />;
export const Primary = Template.bind({});
Primary.args = { ...args };\n""")
    story_file_writer.write(
        t.substitute({
            'comp': comp,
            'prop_str': f"{comp}Props"
        }))
    story_file_writer.close()
    return


# Index boilerplate
def create_index(comp):
    index_file_writer = open(f"{comp_dir}/index.ts", "w+")
    t = Template("export { $comp } from './$comp';")
    index_file_writer.write(t.substitute({'comp': comp}))
    index_file_writer.close()
    return


# Passed both checks
os.mkdir(comp_dir)
create_component(component_name)
create_styles(component_name)
create_index(component_name)
create_story(component_name)
create_test(component_name)
