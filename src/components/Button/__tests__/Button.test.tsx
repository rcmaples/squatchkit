import { render, screen } from '@testing-library/react';
import Button from '../index'

describe("<Button />", () => {
  it('should render a button on the screen', () => {
    render(<Button label="hi" >Hi</Button>);
    expect(screen.getByText('hi')).toBeInTheDocument();
  })
})