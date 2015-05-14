require 'spec_helper'
require 'pacto/rspec'
require 'pacto/test_helper'

describe 'my consumer' do
  include Pacto::TestHelper

  it 'calls a service' do
    with_pacto(
      :port => 8000,
      :live => true,
      :stub => false
    ) do |pacto_endpoint|
      Net::HTTP.get(URI("#{pacto_endpoint}"))
      expect(Pacto).to have_validated(:get, 'http://localhost:8000')
    end
  end
end