from numpy import asarray

from pyanten.Utility import frequencyToWavelength

def samplingLength(frequency):
  r""" Maximum sampling length for near-field antenna measurements

  Parameters
  ----------
  frequency : array_like [float]
      frequency of interest in Hertz [Hz]

  References
  -----
  .. [1] IEEE 149-2021 Recommended Practice for Antenna Measurements, Section 12.5, Page 134.
  .. [2] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.2.5, Page 23, Equation 25.

  Formula
  -------
  .. math::
      \Delta = \lambda / 2 = 0.5 \times (c_0 / f)
  """
  Delta = 0.5*asarray(frequencyToWavelength(frequency))
  return Delta.tolist()